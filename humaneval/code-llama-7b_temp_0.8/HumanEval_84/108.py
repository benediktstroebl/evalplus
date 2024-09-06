
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

    # First, convert N to a string of binary digits
    #   For example, if N = 5, then the binary digits are [1,0,1]
    binary_digits = []
    while N > 0:
        N, remainder = divmod(N, 2)
        binary_digits.append(str(remainder))

    # Next, get the sum of the binary digits and convert to a string
    binary_digit_sum = sum(int(d) for d in binary_digits)
    return str(binary_digit_sum)

