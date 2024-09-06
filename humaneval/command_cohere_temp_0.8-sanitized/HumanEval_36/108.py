def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results
    counts = [0] * (n + 1)
    # Initialize count at 0 for the value of 0
    counts[0] = 0
    for i in range(1, n + 1):
        # For each number less than n, update the count of 7 if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            counts[i] += counts[i - 1] + digits_with_seven(i)
    return counts[n]
def digits_with_seven(n):
    """Return the number of times the digit 7 appears in the integer n."""
    return n // 10 * (n % 10 == 7)