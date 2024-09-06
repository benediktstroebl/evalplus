def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results
    results = [0, 0, 0]

    # Loop through values less than n up to n - 1
    for i in range(n):
        # Calculate the decimal representation of the number
        num = f"{i}:".replace('.', '').replace('^', '').replace('×', '').replace('÷', '')
        
        # Check if the number is divisible by 11 or 13
        if int(num) % 11 == 0 or int(num) % 13 == 0:
            # Count the number of 7s
            results[-1] += sum(1 for x in str(i) if x == '7')

    # Return the maximum value from the results array
    return max(results)