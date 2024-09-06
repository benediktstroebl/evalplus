
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
    def bit_sum(number):
        """Computes the total sum of all bits of a number.

        :param number: a positive integer number
        :returns: the sum of all bits of the input number
        """
        if number == 0:
            return 0
        return bit_sum(number // 2) + number % 2

    return bin(bit_sum(N))[2:]
