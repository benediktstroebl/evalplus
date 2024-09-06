def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results
    freq = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1]
    # Loop through all numbers from 1 to n
    for i in range(1, n + 1):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Use a customized explicit iteration to count the sevens
            count = 0
            while i != 0:
                if i % 10 == 7:
                    count += 1
                i //= 10
            # Update the frequency count
            freq[count] += 1
    # Return the number of times 7 appears in numbers less than n which are divisible by 11 or 13
    return freq[-1]