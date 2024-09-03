def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(c=='%11' or c=='%13' for c in str(n))