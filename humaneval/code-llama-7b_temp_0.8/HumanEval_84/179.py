
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

    def from_decimal(n):
        bin_digits = []
        while n > 0:
            bin_digits.append(str(n % 2))
            n = n // 2
        bin_digits = bin_digits[::-1]
        return "".join(bin_digits)

    def sum_digits(n):
        s = 0
        for c in n:
            s += int(c)
        return s

    # This solution is not correct. It has to use from_decimal.
    # def sum_digits(n):
    #     s = 0
    #     while n > 0:
    #         s += n % 10
    #         n = n // 10
    #     return s

    bin_digits = from_decimal(N)
    return from_decimal(sum_digits(bin_digits))


