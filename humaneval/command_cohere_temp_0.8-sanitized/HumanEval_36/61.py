def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers less than n, reduce precision error.
    num = [int(x) for x in str(n).split('9')]
    # Filter out numbers not divisible by 11 or 13, with reduced precision error.
    div = [x for x in num if x % 11 == 0 or x % 13 == 0]
    return sum(1 for _ in range(len(div)) if div[len(div) - 1] % 7 == 0)