
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
    # check if N is positive
    if N < 0:
        return "-1"
    
    # check if N is a power of 2
    if N > 0 and N & (N - 1):
        return "0"
    
    # convert N to binary
    binary = str(N)
    
    # reverse the binary string
    binary = binary[::-1]
    
    # convert the digits of binary string to their sum
    total = 0
    for digit in binary:
        total += digit
    
    # convert the sum to binary
    binary = str(total)
    
    # remove leading zeroes
    binary = binary[:-1]
    
    # return the binary number
    return "-1" if total < 0 else binary
