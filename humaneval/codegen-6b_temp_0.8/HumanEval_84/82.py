
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
    count = 1
    res = 0
    if N == 0:
        return '0'
    while count * 2 <= N:
        if N - count * 2 == 0:
            res += 0
            break
        if N - count * 2 > 0:
            res += count
            N = N - count * 2
        count *= 2
    if N != 0:
        res += N
    return str(res)
