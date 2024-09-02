
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
    # convert n to binary and sum the digits
    binary_str = str(N)
    sum_str = '0'
    while binary_str:
        left_str = binary_str[:2]
        sum_str = sum_str + left_str[1]
        binary_str = binary_str[2:]
    return sum_str
