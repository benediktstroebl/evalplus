
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
    # variable to store the sum of digits
    sum = 0
    
    # iterate over digits of N
    for i in range(10):
        # get the digits of N
        digits = str(N)
        
        # store each digit as a variable
        digits = digits[i]
        
        # add the digit to the sum
        sum += digits
        
    # convert sum to binary and return as a string
    binary = str(sum)
    
    return binary
