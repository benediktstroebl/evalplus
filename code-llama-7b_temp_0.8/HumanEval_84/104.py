
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
    binary_string = ""
    while N > 0:
        remainder = N % 2
        N = N // 2
        total = total + remainder
    while total > 0:
        remainder = total % 2
        total = total // 2
        binary_string = binary_string + str(remainder)
    return binary_string

