
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    # get the digits of x
    # split x into an array of digits, and reverse the array
    # use the list slicing operator [:]
    # use the string join method to concatenate the array into a string
    num_arr = list(str(x))
    num_arr.reverse()
    num_str = ''.join(num_arr)
    # return the first shift chars of num_str
    # use the list slicing operator [start:stop:step]
    # use the integer modulo to determine the length of the string
    return num_str[shift % len(num_str):]

