def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers divisible by 11 or 13 and count sevens
    return sum(7 in str(x) for x in range(1, n+1) if not (x % 11 == 0 or x % 13 == 0))