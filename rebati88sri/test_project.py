# test_atm_simulator.py
import pytest
from project import (
    check_pin, deposit, withdraw,
    change_pin, check_balance,
    print_history, currency_converter
)

def test_check_pin():
    assert check_pin(1234, 1234)
    assert not check_pin(1111, 1234)

def test_deposit():
    balance, history = 1000, []
    new_balance, msg = deposit(balance, 500, history)
    assert new_balance == 1500
    assert "Deposit successful" in msg
    assert len(history) == 1

    new_balance, msg = deposit(new_balance, -100, history)
    assert new_balance == 1500
    assert "Invalid deposit amount" in msg

def test_withdraw():
    balance, history = 2000, []
    new_balance, msg = withdraw(balance, 1000, history)
    assert new_balance == 1000
    assert "Withdrawal successful" in msg
    assert len(history) == 1

    new_balance, msg = withdraw(new_balance, 3000, history)
    assert new_balance == 1000
    assert "Insufficient funds" in msg

    new_balance, msg = withdraw(new_balance, 123, history)
    assert "multiples of ₹100" in msg

def test_change_pin():
    user = {"pin": 1234}
    result = change_pin(user, 5678)
    assert result == "PIN changed successfully."
    assert user["pin"] == 5678

def test_check_balance():
    output = check_balance(1500)
    assert "₹1,500.00" in output

def test_print_history():
    assert print_history([]) == "No transactions yet."
    history = ["Deposited ₹500"]
    assert "Deposited" in print_history(history)

def test_currency_converter():
    usd = currency_converter(8300)
    assert "$100.00" in usd
