
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
    """
    >>> solve(1000)
    '1'
    >>> solve(150)
    '110'
    >>> solve(147)
    '1100'
    >>> solve(1001)
    '10000'
    >>> solve(1234)
    '10100'
    """
    assert 0 <= N <= 10000, 'Invalid input'
    str_binary = ''
    while N > 0:
        str_binary += str(N % 2)
        N = N // 2
    return str_binary[::-1]
    
    
