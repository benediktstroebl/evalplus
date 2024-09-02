
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
    # variable to store the sum of digits
    digits = str(N)
    # remove the trailing zero from the string
    digits = digits[:-1]
    # convert the string to a binary number
    binary = 0
    for digit in digits:
        binary += digit * 2**(len(digit) - 1)
    # reverse the binary number
    binary = binary[::-1]
    # convert the binary number to a decimal number
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2**(len(binary) - i - 1))
    # subtract the decimal number from the original number
    return N - decimal
