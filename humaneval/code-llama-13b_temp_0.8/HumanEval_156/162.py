
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    # keep track of the digits to build the roman numeral string
    result = ''
    # we will work our way from the "ones" digit to the "thousands" digit
    # going in reverse, so "1234" becomes [4, 3, 2, 1]
    digits = list(str(number))[::-1]
    # for each digit, we'll use this to scale up the value
    scale_values = [1000, 100, 10, 1]
    for i, digit in enumerate(digits):
        # convert each digit to an integer
        digit_value = int(digit)
        # get the corresponding scale value
        scale_value = scale_values[i]
        # get the corresponding number of "M" characters
        result += (digit_value // scale_value) * 'm'
        # if we have a remainder, we'll need to adjust the scale value
        # and get the correct roman numeral values
        digit_value = digit_value % scale_value
        if digit_value == 9:
            scale_value /= 10
            result += 'm' + (scale_value // 10) * 'i' + (scale_value % 10) * 'x'
        elif digit_value == 4:
            scale_value /= 10
            result += 'm' + (scale_value // 10) * 'i' + (scale_value % 10) * 'iv'
        elif 0 < digit_value < 5:
            scale_value /= 10
            result += 'm' + (scale_value // 10) * 'i' + digit_value * 'v'
        elif 5 <= digit_value < 9:
            scale_value /= 10
            result += 'm' + (scale_value // 10) * 'i' + (digit_value - 5) * 'x'
        elif digit_value == 0:
            # nothing to do
            pass
    return result.lower()

