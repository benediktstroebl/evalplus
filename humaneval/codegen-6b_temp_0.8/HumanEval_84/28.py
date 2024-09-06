
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
    # Write your code here
    total = 0
    for i in range(0, 10):
        _dir = str(2**i)
        if len(_dir) > N:
            _dir = str(2**i)[-N:]
        total += int(_dir)
    return total
