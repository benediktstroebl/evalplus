def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results
    count = 0
    results = []

    # Loop through numbers less than n
    for i in range(n + 1):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Check if the number contains the digit 7
            if 7 in str(i):
                count += 1
        # Store the results
        results.append(count)

    return results