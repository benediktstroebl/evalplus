
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
    # use 0/1 as binary
    ret = ''.join(map(str, [int(x) for x in bin(N)[2:]]))
    return '0' * (4 - len(ret)) + ret

assert solve(1000) == '1'
assert solve(147) == '1110'
assert solve(10000) == '0'
