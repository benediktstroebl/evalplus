
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # convert integer to string and then to list
    str_list = list(str(x))
    # length of list
    length = len(str_list)
    # create a new list for the output
    output = list()
    # check if shift is smaller than length
    if shift <= length:
        for i in range(length - shift, length):
            # append the reversed value to the end
            output.append(str_list[i])
        # reverse the output
        output.reverse()
    else:
        # create a new list from the original one
        # without the last value
        str_list.pop()
        # reverse the list
        str_list.reverse()
        # append the new list to the output
        for i in range(0, length):
            output.append(str_list[i])
    return "".join(output)

