
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

    def digits_to_bin(num):
        bin_str = ""
        while num:
            num, remainder = divmod(num, 2)
            bin_str = str(remainder) + bin_str
        return bin_str

    bin_str = digits_to_bin(N)
    return sum(int(digit) for digit in bin_str)

