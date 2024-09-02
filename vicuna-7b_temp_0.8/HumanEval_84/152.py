
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
    digits = []
    total = 0
    while N > 0:
        digit = N % 10
        digits.append(digit)
        N = N / 10
        total += digit
    reversed_digits = reversed(digits)
    binary_string = "".join(reversed_digits)
    return binary_string
