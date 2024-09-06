def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results of integer divisions by 11 and 13.
    counts = [0, 0]
    for i in range(1, n + 1):
        # Determine if the current number is divisible by 11 or 13.
        for j in range(2):
            if i % (11 * j) == 0 and i % 13 == 0:
                # Increment the count of 7s if the current number is divisible by 11 * j or 13.
                counts[j] += int(str(i)[-1] == '7')
    return max(counts)