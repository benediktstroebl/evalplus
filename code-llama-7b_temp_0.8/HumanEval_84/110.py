
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
    
    # define a function that converts an integer to binary number
    def int_to_binary(integer):
        # if the integer is zero
        if integer == 0:
            # return 0
            return '0'
        # initialize an empty string
        binary = ''
        # find the remainder
        remainder = integer % 2
        # while the integer is greater than zero
        while integer > 0:
            # add the remainder to the binary string
            binary += str(remainder)
            # divide the integer by two
            integer //= 2
            # find the remainder
            remainder = integer % 2
        # return the binary string in reverse order
        return binary[::-1]
    
    # define a function that returns the sum of the digits in a binary number
    def sum_binary_digits(binary):
        # initialize a running sum to zero
        running_sum = 0
        # for each character in the binary string
        for digit in binary:
            # convert the character to an integer
            digit = int(digit)
            # add the digit to the running sum
            running_sum += digit
        # return the running sum
        return running_sum
    
    # define a function that concatenates a string with binary digits
    def concat_digits(binary, string):
        # if the binary string is not empty
        if binary:
            # find the sum of the digits in the binary string
            running_sum = sum_binary_digits(binary)
            # if the running sum is greater than 0
            if running_sum > 0:
                # concatenate the string with the running sum in binary
                string += str(bin(running_sum)[2:])
            # otherwise
            else:
                # concatenate the string with 0
                string += '0'
        # return the concatenated string
        return string
    
    # initialize an empty string
    result = ''
    # convert N to a binary string
    binary_N = int_to_binary(N)
    # concatenate the result with the binary string
    result = concat_digits(binary_N, result)
    # return the result
    return result
    
