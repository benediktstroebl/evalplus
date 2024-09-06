def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results of indexing the digits
    count = []
    # Loop through numbers less than n
    for i in range(1, n + 1):
        # Check if the current number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Extract the digit at index 3, which is the fourth digit (0-indexed)
            digit = int(str(i)[3])
            # Increment the count if the digit is 7
            if digit == 7:
                count.append(1)
            else:
                count.append(0)
    return sum(count)