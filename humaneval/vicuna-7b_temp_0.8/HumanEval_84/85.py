
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
    sum = 0
    for n in range(N):
        while N > 0:
            if N % 2 == 0:
                N = N // 2
                sum = sum * 10 + (N % 10)
            else:
                N = N // 2
                sum = sum * 10 + (N % 10)
    return sum
