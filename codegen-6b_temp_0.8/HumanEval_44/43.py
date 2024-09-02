

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # convert number to string
    temp = str(x)
    # find the length of string
    length = len(temp)
    # convert to array
    arr = [int(i) for i in temp]
    # calculate result
    result = arr[0]
    for i in range(1, length):
        result = result * base + arr[i]
    return str(result)
