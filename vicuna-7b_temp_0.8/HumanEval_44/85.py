

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
    # Convert input number to base 10
    number = str(x)
    # Convert number to desired base
    result = ''
    while number:
        # Get digit at current position
        digit = number[0]
        # If digit is greater than base or current position is at the end of the number,
        # increment the base and move to the next position
        if digit > base or digit == number[-1]:
            result += str(digit - 10)
            number = number[1:]
        else:
            result += digit
            # If this is the last digit, append the number
            if len(number) == 0:
                result += str(number)
    return result
