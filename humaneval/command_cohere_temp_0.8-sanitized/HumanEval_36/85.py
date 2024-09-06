def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers with 7 in them and divisible by 11 or 13
    return sum(1 for num in range(n) if 7 not in str(num) and (num % 11 == 0 or num % 13 == 0))