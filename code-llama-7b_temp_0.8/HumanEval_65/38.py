
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    """
    x = int(input("Enter your number: "))
    shift = int(input("Enter the shift value: "))

    x = int(x)
    shift = int(shift)
    if shift >= len(x):
        return str(x[::-1])
    else:
        return str(x[-shift:])+ str(x[:-shift])
    """
    num = str(x)
    x = list(num)
    shift = shift % len(x)
    shift = shift if shift >= 0 else shift + len(x)
    result = x[shift:] + x[:shift]
    return "".join(result)
