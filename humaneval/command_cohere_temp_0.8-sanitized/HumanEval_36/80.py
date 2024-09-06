def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results of integer divisions by 11 and 13.
    divisible_by_11_or_13 = []
    
    # Utilize a for loop to iterate through integers from max(1, n - 1) to n inclusive.
    for num in range(max(1, n - 1), n + 1):
        # Determine if the current integer is divisible by 11 or 13.
        if num % 11 == 0 or num % 13 == 0:
            # If the digit 7 exists in the current integer, increment the count by 1.
            if 7 in str(num):
                divisible_by_11_or_13.append(1)
            else:
                divisible_by_11_or_13.append(0)
    
    # Calculate the total count of 7's in the integers divisible by 11 or 13.
    total_seven_count = sum(divisible_by_11_or_13)
    
    # Return the total count of 7's.
    return total_seven_count