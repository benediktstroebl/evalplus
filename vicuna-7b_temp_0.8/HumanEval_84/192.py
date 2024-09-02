
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
    N = int(N)
    if N < 2 or N > 10000:
        return "0"
    sum = 0
    while N:
        carry = 0
        while N > 9:
            N = N / 10
            carry += N % 10
        N = N / 10
        sum += carry
        carry = 0
    return sum
