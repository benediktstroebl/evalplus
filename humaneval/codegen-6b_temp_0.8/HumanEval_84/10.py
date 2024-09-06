
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
    # base-2 number representation of the input integer
    from math import log2
    bin_num = bin(N)
    bin_num = int(bin_num[2:])
    # sum of digits.
    sum_digits = 0
    for digit in str(bin_num):
        sum_digits += int(digit)
    return bin_num

assert solve(1000) == "1"
assert solve(150) == "110"
assert solve(147) == "1100"
assert solve(12) == "1000"
assert solve(15) == "1001"
assert solve(126) == "101001"

from test_util import assert_equals
assert_equals(solve(234), "10101")
