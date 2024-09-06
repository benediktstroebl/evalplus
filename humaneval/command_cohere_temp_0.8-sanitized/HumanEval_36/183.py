def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results
    counts = [0] * (n + 1)
    # Initialize count at 0 for the number 7
    counts[7] = 0
    # Calculate the counts of 7 for numbers from 1 to n
    for i in range(1, n + 1):
        if i % 11 == 0 or i % 13 == 0:
            counts[i] += counts[i % 10]
    return counts[7]