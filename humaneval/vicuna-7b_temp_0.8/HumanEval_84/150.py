
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
    # format string
    pattern = "{}{}{}"
    # convert n to binary
    bin_n = str(N).zfill(base=2)
    # format string
    pattern = "{}{}{}"
    # convert sum to binary
    bin_sum = "".join(str(x) for x in sum(int(x) for x in bin_n))
    return pattern.format(bin_n, bin_sum, bin_n[:2])
