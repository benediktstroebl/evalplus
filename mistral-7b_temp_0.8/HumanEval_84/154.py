
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
    from math import log2
    while N > 0:
        num = N % 2
        N = N // 2
        if num != 0:
            result = str(num)
        else:
            result = '0'
        binary = ''
        while len(result) < log2(N) + 1:
            result = '0' + result
        for i in result:
            binary += i
    return binary[::-1]
