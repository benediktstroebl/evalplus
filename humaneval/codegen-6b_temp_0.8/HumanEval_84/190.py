
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
    def helper(n):
        """Helper function to convert n to binary and sum the digits in it."""
        if n == 0:
            return
        helper(n // 2)
        result = str(n % 2)
        sum_digits(result)

    def sum_digits(result):
        """Calculate the sum of digits of result."""
        bin_number = int(result, 2)
        if bin_number == 0:
            return
        sum_str = str(bin_number)
        sum_digits_helper(sum_str)

    def sum_digits_helper(sum_str):
        """Helper function to calculate sum of digits of sum_str."""
        sum_digits_helper(sum_str[1:])
        if sum_str[0] == '1':
            sum_digits_helper(sum_str[1:])
            sum_digits_helper(sum_str)

    helper(N)
    return result # Example: 101 = 1 + 2 + 4 + 8 = 11 in binary

