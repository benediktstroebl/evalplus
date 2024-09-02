
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
    if N == 0:
        return "0"

    # convert to binary, right padding with zero
    binary = bin(N)[2:].zfill(16)

    # iterate the string, 
    #   subtract 0b1010 from 0b1111111111111111
    #   bitwise & 0b0111111111111111
    result = 0b0
    for c in binary:
        if c == '1':
            result = (result - 0b1010) & 0b0111111111111111
        else:
            result = (result + 0b1010) & 0b0111111111111111
    
    # convert to binary, right padding with zero
    result = bin(result)[2:].zfill(16)

    # return the last 4 bits of the binary string
    return result[-4:]






