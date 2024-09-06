def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out the numbers less than n and divisible by 11 or 13
    counts = [(7 in divmod(i, 11).digits or 7 in divmod(i, 13).digits) for i in range(n+1)]
    # Filter out the counts for numbers greater than n or not divisible by 11 or 13
    return sum(count for count in counts if count == True)