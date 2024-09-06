
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
    # Take the first digit, convert to binary, get the sum of the digits, 
    # and keep doing this with the rest of the digits.
    sum = 0
    while N > 0:
        d = N % 2
        N //= 2
        sum += d
    # Convert to binary.
    s = ''
    while sum > 0:
        d = sum % 2
        sum //= 2
        s += str(d)
    return s
    
