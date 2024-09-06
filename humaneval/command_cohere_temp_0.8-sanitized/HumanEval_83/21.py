def starts_one_ends(n):
    # Create a list to store the digits
    num_digits = [0, 0, 0, 0, 0]
    
    # Iterate through each possible digit from 0 to 9
    for digit in range(1, n + 1):
        # Create a temporary list to store the number of digits
        temp_num_digits = [0, 0, 0, 0, 0]
        
        # Calculate the new count of digits for the current digit at the start or end
        for i in range(n - digit + 1):
            temp_num_digits[0] = temp_num_digits[0] + 1 if (i == 0 or i == n - digit) else 0
            temp_num_digits[1] = temp_num_digits[1] + 1 if (i == 1 or i == n - digit - 1) else 0
            temp_num_digits[2] = temp_num_digits[2] + 1 if (i == 2 or i == n - digit - 2) else 0
            temp_num_digits[3] = temp_num_digits[3] + 1 if (i == 3 or i == n - digit - 3) else 0
            temp_num_digits[4] = temp_num_digits[4] + 1 if (i == 4 or i == n - digit - 4) else 0
        
        # Add the calculated digits to the original list
        for i in range(5):
            num_digits[i] = num_digits[i] + temp_num_digits[i]
    
    # Return the sum of the digits
    return sum(num_digits)