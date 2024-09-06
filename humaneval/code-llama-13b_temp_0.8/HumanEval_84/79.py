
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
    # Number of bits
    # binary number = "01001"
    # len(binary number) = 5
    # bit = 5
    bit = len(bin(N)[2:])

    # Find the max number that can be expressed as bit
    max_number = 2**bit - 1

    # Convert the binary number to decimal
    # binary_number = "01001"
    # bin2dec("01001") = 5
    binary_number = bin2dec(bin(N)[2:])

    # Get the sum
    # sum = max_number + binary_number - max_number
    sum = binary_number + max_number

    # Convert back to binary
    # dec2bin(sum) = "10011"
    return dec2bin(sum)

