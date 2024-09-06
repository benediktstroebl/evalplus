def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results of integers less than n and divisible by either 11 or 13.
    freq = [7, 10, 6, 5, 6, 10, 5, 10, 7, 12, 3, 10, 5, 2, 7, 10, 4, 7]
    return sum(freq[:n]) if n < len(freq) else 0