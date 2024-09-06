
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
    def binary_sum(a,b):
        return '{:b}'.format(a+b)
    def binary_digit(num,i):
        if num == 0:
            return ''
        return '1' + binary_digit(num//2, i-1) if i != 0 else binary_digit(num//2, i-1)
    return binary_digit(N,len(bin(N)[2:])-1)
