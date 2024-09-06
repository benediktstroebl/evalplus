def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results
    results = [0, 0, 0]

    # Loop through integers from 0 to  n.
    for i in range(n + 1):
        # Check if the current integer is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Count the number of 7s in the current integer
            results[0] += int(i / 7)
            results[1] += int(i / 17)
            results[2] += int(i / 71)

    # Return the sum of results
    return results[0] + results[1] + results[2]