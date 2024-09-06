def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers less than n and divisible by 11 or 13, then count sevens.
    return sum(7 in str(x) for x in range(n+1) if (x % 11 == 0 or x % 13 == 0))