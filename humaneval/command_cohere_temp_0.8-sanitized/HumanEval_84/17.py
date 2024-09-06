def solve(N):
    # Convert the integer to a binary string
    bin_str = bin(N)[2:]
    
    # Initialize the sum of digits to 0
    sum_digits = 0
    
    # Loop through each digit in the binary representation
    for digit in bin_str:
        # Convert the digit to an integer (remove leading zeros)
        digit_int = int(digit)
        sum_digits += digit_int
    
    return format(sum_digits, 'b')