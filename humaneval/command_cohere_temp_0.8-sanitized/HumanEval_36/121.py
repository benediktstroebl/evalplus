def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results
    counts = [0] * (n + 1)
    # Initialize the count at index 0 to 1 (7 is found in 77)
    counts[0] = 1
    for i in range(1, n + 1):
        # Check if the current index is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Count the occurrences of 7 in the current index
            counts[i] = counts[i - 1] + (7 in str(i))
        # Handle cases where i = 77 and i = 88
        elif i == 77:
            counts[i] = 2
        elif i == 88:
            counts[i] = 1
    # Return the last count, which is the result for the given n
    return counts[-1]