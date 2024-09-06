def solve(N):
    # Convert the integer to a string
    N_str = str(N)
    
    # Initialize the sum of digits in binary to an empty string
    result = ''
    
    # Loop through each digit in the integer
    for digit in N_str:
        # Convert the digit to a binary string
        digit_bin = bin(int(digit))[2:]
        
        # Append the binary representation of the digit to the result
        result += digit_bin
    
    # Return the result
    return result