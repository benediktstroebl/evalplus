
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

    
    result = ''
    if N == 0:
        return '0'
    elif N == 1:
        return '1'
    elif N == 2:
        return '10'
    else:
        while True:
            if N > 1:
                N = int(N / 2)
                result += str(N)
            else:
                result = result[::-1]
                return result
            
            
            
    
