
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    # Get the binary representation of N
    binary_N = str(N)
    binary_N_length = len(binary_N)
    
    # Initialize result
    result = ""
    
    # Check if N has only one digit
    if binary_N_length == 1:
        result = binary_N[0]
    
    # Check if N has two digits
    else:
        # Get the first digit of N
        first_digit = binary_N[0]
        
        # Get the next digit if it exists
        next_digit = binary_N[1]
        
        # Append the first digit to result
        result += first_digit
        
        # Add the sum of digits of N
        if next_digit == "0":
            result += "1"
        else:
            result += "1"
            sum_of_digits_next = get_sum_of_digits(next_digit)
            result += str(sum_of_digits_next)
    
    return result
