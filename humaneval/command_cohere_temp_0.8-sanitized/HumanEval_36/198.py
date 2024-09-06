def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out the numbers from 1 to n that are divisible by 11 or 13.
    bins = [i for i in range(1, n + 1) if i % 11 == 0 or i % 13 == 0]
    # Count the number of times digit 7 appears in the list of eligible numbers.
    return sum(1 for _ in bins if _.toString().includes('7'))