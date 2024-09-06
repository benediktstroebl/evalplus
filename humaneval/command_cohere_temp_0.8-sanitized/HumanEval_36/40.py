def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers divisible by 11 or 13 and count sevens
    return sum(int(d) == 7 for num in range(1, n + 1) for d in str(num) if num % 11 == 0 or num % 13 == 0)