
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
    def sum_of_digits(n):
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s
    
    return ''.join([str(sum_of_digits(n)) for n in range(1, N+1)])
