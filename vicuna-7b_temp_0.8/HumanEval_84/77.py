
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
    # digits = list(map(str, [N//100, N//10, N//1, 1]))
    digits = [str(int(N//100)) + str(int(N//10) % 10) + str(int(N//1) % 10) + str(int(N) % 10) + '0'*(N//1 % 10)]
    return ''.join(digits)
