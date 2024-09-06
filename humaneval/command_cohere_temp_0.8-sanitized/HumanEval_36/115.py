import unittest
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results of integer divisions by 11 and 13.
    divisible_by_11_or_13 = [divmod(i, 11).sum() + divmod(i, 13).sum() for i in range(1, n + 1)]
    # Use a list comprehension to count the number of times 7 appears in `divisible_by_11_or_13`.
    return sum(7 in num for num in divisible_by_11_or_13)