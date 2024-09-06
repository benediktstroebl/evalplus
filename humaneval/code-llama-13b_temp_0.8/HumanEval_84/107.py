
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
    def binary_sum(N):
        """Return the sum of digits of N in binary."""
        sum = 0
        while N:
            # Make a bitwise AND of N with 00000001
            # then shift it to the right by 1
            sum += (N & 1)
            N >>= 1
        return sum
    return format(binary_sum(N), 'b')

