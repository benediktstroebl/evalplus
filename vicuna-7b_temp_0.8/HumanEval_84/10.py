
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
    # Convert N to binary
    n = str(N)
    # Initialize the result to 0
    result = 0
    # Iterate over the digits of n
    for d in n:
        # If the digit is 0, add the next digit of n
        if d == '0':
            result += n[1]
        # Add the current digit to the result
        result += d
    # Add the 0s at the end of the result
    result = ''.join([str(digit) for digit in result])
    return result
