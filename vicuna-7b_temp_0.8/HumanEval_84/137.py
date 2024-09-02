
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
    digits = [str(N)[2:].zfill(2) for _ in range(log2(N))]
    for digit in digits:
        sum += digit
    return '1' + '0'*7 if sum == 0 else sum%10 + '1' + '0'*9
