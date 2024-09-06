
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    #Return x if shift is greater than x's length.
    if shift > len(str(x)):
        return str(x)[::-1]
    #Build the string of numbers that are to be shifted.
    num = str(x)
    #Build the string that will be returned.
    res = ""
    #Store the index of the last digit to be shifted.
    last_shift = num.index(num[-1])
    #If shift is greater than the last digit, the digits need to be shifted right.
    if shift > last_shift:
        #Slice the number to be shifted starting from last digit to 0.
        num = num[last_shift:] + num[:last_shift]
    #Iterate through the number to be shifted.
    for i in range(last_shift, len(num)):
        #Slice the number to be shifted starting from i to 0.
        num = num[i:] + num[:i]
        #Add the next digit in the number that is to be shifted to the result.
        res += num[0]
        #Shift the
