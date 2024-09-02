
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
    m = max(math.ceil(math.log(N, 2)), 0)
    
    i, summary = 0, 0
    
    while i < m:
        if i == 0:
            summary += N % 2
        else:
            summary += N // (2**i) % 2
        i += 1
    
    return str(summary)