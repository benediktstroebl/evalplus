
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # find the number of digits in x
    # by converting it to a string and then
    # finding the length of the string
    # or by using the fact that the number of digits
    # is one more than the floor of the log base 10 of x
    #digits = len(str(x))
    #digits = int(1 + math.log10(abs(x)))
    digits = (1+int(math.log(abs(x), 10)))

    # if the number of digits is less than shift
    # then reverse the digits
    if digits < shift:
        x = int(str(x)[::-1])
        return str(x)
    else:
        # the string representation of x
        s = str(x)

        # remove the first shift characters by slicing s
        # and then concatenate the shift first characters
        # to the end of the string
        s = s[shift:] + s[:shift]

        return s
