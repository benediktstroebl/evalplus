
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
    ROMAN = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    index = 0
    digits = [int(digit) for digit in str(number)]
    result = []
    while index < len(digits):
        current_digit = digits[index]
        while index < len(digits) and current_digit == digits[index]:
            index += 1
        current_value = current_digit * ROMAN[index - 1][0]
        if current_value > ROMAN[index - 1][0]:
            current_value = ROMAN[index - 1][0] + ROMAN[index - 1][1]
        result.append(current_value)
    return ''.join(result)

