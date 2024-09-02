
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # a=str(x)
    # b=len(a)
    # if shift>b:
    #     for i in range(b):
    #         a[i]+=a[i+1]
    #         return a[-1]
    # else:
    #     for i in range(b-shift):
    #         a[i]+=a[i+shift]
    #         return a[shift:-1]

    return str(x)[(-shift):]+str(x)[:(-shift)] if shift<len(str(x)) else str(x)[::-1]
    # TODO: Implement this correctly.


