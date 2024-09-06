def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results
    counts = [0] * (n + 1)
    
    # Iterate through numbers less than n and divisible by 11 or 13
    for num in range(1, n + 1):
        if num % 11 == 0 or num % 13 == 0:
            # Count the occurrences of 7 in the current number
            counts[num] = num % 10 == 7
    
    # Sum the counts of 7s for numbers divisible by 11 or 13
    return sum(counts)