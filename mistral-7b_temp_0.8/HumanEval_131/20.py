
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    output=0
    # convert the integer to a string
    number_str = str(n)
    # loop through the string
    for i in range(0,len(number_str)):
        # get the current character
        digit = number_str[i]
        # convert the current character to an integer
        digit_int = int(digit)
        # check if the current digit is even
        if digit_int % 2 != 0:
            output = output*digit_int
    return output

