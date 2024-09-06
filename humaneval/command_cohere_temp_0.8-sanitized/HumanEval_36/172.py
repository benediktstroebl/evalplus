def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results
    counts = [0] * (n + 1)
    # Initialize count at 0 for the integer 1
    counts[1] = 0
    # Calculate and store the counts of 7 in divisible by 11 or 13 in the range 1 to n
    for i in range(1, n + 1):
        if i % 11 == 0 or i % 13 == 0:
            counts[i] += (i // 10) * ('7' in str(i))
        # Handle case where i is divisible by both 11 and 13
        if i % 121 == 0:
            counts[i] += 2 * ('7' in str(i))
    return counts[n]