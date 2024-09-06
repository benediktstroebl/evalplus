
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
    
    # Initialize result string
    result = ''
    
    # Convert the number to binary, 10 digits in total
    for i in range(10):
        # Get the remainder of the division
        rem = N % 2
        # Append to the result
        result += str(rem)
        # Discard the last digit
        N = N // 2
        
    # Return the result
    return result
