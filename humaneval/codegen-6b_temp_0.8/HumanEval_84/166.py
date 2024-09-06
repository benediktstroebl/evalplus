
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
    b = []
    x = 0
    while x < 10:
        b = int(N / 2)
        x = int(x + b)
        N = int(N - (2 * b))
    
    if b == 1 or b == 0:
        b = 0
    if b == 0:
        return bin(1)[2:].strip('0')
    return bin(b)[2:].strip('0') 


