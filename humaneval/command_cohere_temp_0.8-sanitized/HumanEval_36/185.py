def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results
    counts = [0] * (n + 1)
    half_limit = (n + 1) // 2
    
    for i in range(1, half_limit):
        if i % 11 == 0 or i % 13 == 0:
            # Count the occurrences of digit 7 in the current number
            current_7s = numeral_seven(i)
            
            # Update the count for the current number and fizz-buzz limit
            counts[i] = current_7s
            if i <= n:
                counts[n] += current_7s
    
    return counts[n]
def numeral_seven(n):
    """Return the number of times the digit 7 appears in n."""
    return n // 10 * (n % 10 == 7)