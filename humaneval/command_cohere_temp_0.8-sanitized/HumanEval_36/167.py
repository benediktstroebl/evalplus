def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers with 7 and divisible by 11 or 13 from the range below n
    count = sum(1 for num in range(n) if 7 in str(num) and num % 11 == 0 or num % 13 == 0)
    return count