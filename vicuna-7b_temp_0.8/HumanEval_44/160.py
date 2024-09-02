

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
    # convert x to a string, since that's how we represent numbers internally
    x = str(x)

    # check if the number of digits in x is less than or equal to base
    if len(x) <= base:
        return x

    # split x into its digits, and put them in reverse order
    digits = [int(d) for d in reversed(x)]

    # calculate the number of times each digit should be multiplied by the base to get the original number
    multipliers = [1] * base
    for i in range(1, base):
        multipliers[i] = int(digits[0]) // i

    # multiply the digits together and add the multipliers to get the original number
    return ''.join(str(d) * i for i, d in enumerate(digits[1:], start=1)) + ''.join([str(m) for m in multipliers])
