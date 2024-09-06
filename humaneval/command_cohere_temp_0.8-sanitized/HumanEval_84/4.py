def solve(n):
    """
    This function takes a positive integer n as input and converts it into a binary string. It accomplishes this by first converting the integer n to a string, s. Then, it iterates through each character in s, where each character represents a digit in the decimal representation. It uses bitwise XOR (^) with 1 to convert each digit to its binary counterpart. XOR with 1 flips the bits of the digit (e.g., 5 becomes 101, while 6 becomes 110). The resulting binary digits are concatenated together to form the final binary string. This approach ensures that the total sum of the digits in binary corresponds to the binary representation of the original number.
    """
    s = str(n)
    return ''.join([str(int(s[i:i+1]) ^ 1) for i in range(len(s))])