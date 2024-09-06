def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results of integer divisions by 11 and 13.
    divisible_by_11_or_13 = []
    
    # Utilize a for loop to iterate through integers from 1 to n.
    for num in range(1, n + 1):
        # Determine if the current integer is divisible by 11 or 13.
        if num % 11 == 0 or num % 13 == 0:
            # If the integer is divisible by 11 or 13, add it to the list.
            divisible_by_11_or_13.append(num)
    
    # Count the number of times the digit 7 appears in the list.
    seven_count = divisible_by_11_or_13.count(7)
    
    # Return the count of the digit 7.
    return seven_count