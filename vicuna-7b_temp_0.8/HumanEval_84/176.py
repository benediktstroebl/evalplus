
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
    total = 0
    while N > 0:
        while N >= 2:
            total += total // N % 2
            N -= 1
        total += N % 2
    return ''.join(str(digit) for digit in total)

input = int(input())
N = input
