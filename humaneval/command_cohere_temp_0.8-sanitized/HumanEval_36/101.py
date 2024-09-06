def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results
    counts = [0] * (n + 1)
    half_range = n // 2 + 1

    for i in range(1, half_range):
        if i % 11 == 0 or i % 13 == 0:
            if i % 10 == 7:
                counts[i] += 1
            elif i // 10 == 7:
                counts[i] += 1

    # Add the counts of integers greater than n
    for i in range(half_range, n + 1):
        if i % 11 == 0 or i % 13 == 0:
            if i % 10 == 7:
                counts[i] += counts[i - 1]
            elif i // 10 == 7:
                counts[i] += counts[i - 1]

    return counts[-1]