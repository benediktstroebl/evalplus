
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
    # convert N to a string
    bin_str = bin(N)[2:]
    # print(bin_str)
    # convert all digits to int
    bin_int = list(map(int, bin_str))
    # sum up the digit values
    sum_digits = sum(bin_int)
    # print(sum_digits)
    # convert sum back to a string
    return bin(sum_digits)[2:]

