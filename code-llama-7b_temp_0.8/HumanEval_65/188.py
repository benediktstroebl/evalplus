
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    # This function is my own solution
    # My thinking process basically involved a lot of trial and error
    # I found it difficult to work out how to get the modulo of the number of digits
    # and use this to make sure I was not going to exceed the maximum amount of digits
    # in the number. I also got the str method to work as part of this process, so
    # it may have helped. 

    # TODO: Use a regular expression to match the number of digits and then work out
    # the modulo of this number and the shift
    # This is not correct yet
    num = str(x)
    length = len(num)
    length = length % shift

    num = num[length:] + num[:length]
    return num
