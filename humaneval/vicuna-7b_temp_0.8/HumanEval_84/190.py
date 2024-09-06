
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
    # check for empty input
    if not N:
        return "0"
    
    # initialize the result string with 0
    result = "0"
    
    # loop through the binary digits of N
    while N:
        # get the leftmost digit of N
        digit = N % 2
        
        # if the current digit is 0, add the value of the next digit to the result string
        if digit == 0:
            digit = N // 2
            result = str(digit) + result
            
        # add the current digit to the result string
        else:
            result += str(digit)
            
        # divide N by 2 to remove the leftmost digit
        N = int(N/2)
        
    return result
