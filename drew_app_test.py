# test_oop_loan_pmt.py

import pytest
from oop_loan_pmt import Loan

# Test data
loan_amount = 100000
years = 30
interest = 0.06
monthly_payment = 599.55

# Unit tests for Loan class methods
class TestLoanClass:
    
    def test_loan_init(self):
        loan = Loan(loan_amount, years, interest)
        assert loan.loan_amount == loan_amount
        assert loan.years == years
        assert loan.interest == interest
        assert loan.monthly_payment == 0  # monthly_payment should be initialized as 0

    def test_loan_calculate_monthly_payment(self):
        loan = Loan(loan_amount, years, interest)
        loan.calculate_monthly_payment()
        assert loan.monthly_payment == pytest.approx(monthly_payment, rel=1e-2)  # Using pytest.approx for float comparison

    def test_loan_get_total_payment(self):
        loan = Loan(loan_amount, years, interest)
        loan.calculate_monthly_payment()
        total_payment = loan.get_total_payment()
        assert total_payment == pytest.approx(monthly_payment * 12 * years, rel=1e-2)  # Total payment should be equal to monthly payment * number of months

# Functional tests for Loan class
def test_loan_functionality():
    loan = Loan(loan_amount, years, interest)
    loan.calculate_monthly_payment()
    assert loan.monthly_payment == pytest.approx(monthly_payment, rel=1e-2)
    total_payment = loan.get_total_payment()
    assert total_payment == pytest.approx(monthly_payment * 12 * years, rel=1e-2)