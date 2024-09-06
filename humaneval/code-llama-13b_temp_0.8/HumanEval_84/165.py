
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
    bn = bin(N)[2:]
    strsum = '0'
    if len(bn) > 1:
        for i in range(len(bn)-1, -1, -1):
            strsum += bn[i]
            strsum = bin(int(strsum,2)+int(bn[i]))[2:]
    return strsum
