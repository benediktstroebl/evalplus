
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
    def binary_to_decimal(binary):
        """Convert binary number to decimal.
        """
        return int(binary, 2)

    def decimal_to_binary(decimal, count):
        """Convert decimal number to binary number.
        """
        result = str(bin(decimal))[2:]
        return result.zfill(count)

    binary = decimal_to_binary(N, len(str(N)))   
    return str(binary_to_decimal(binary))

