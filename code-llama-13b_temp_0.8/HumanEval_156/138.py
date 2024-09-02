
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
    num_to_roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    roman_numeral = ''
    # While there are still number to convert, extract the last digit of the number
    while number > 0:
        # Divide the number by 10 to remove the last digit from number
        digit = number // 10
        if digit == 9:
            roman_numeral += 'x' + num_to_roman['I']
        elif digit == 8:
            roman_numeral += 'i' + num_to_roman['X']
        elif digit == 7:
            roman_numeral += 'i' + num_to_roman['I'] + num_to_roman['X']
        elif digit == 6:
            roman_numeral += 'l' + num_to_roman['X']
        elif digit == 5:
            roman_numeral += 'v' + num_to_roman['I']
        elif digit == 4:
            roman_numeral += num_to_roman['I'] + num_to_roman['V']
        elif digit == 3:
            roman_numeral += num_to_roman['I'] + num_to_roman['I'] + num_to_roman['I']
        elif digit == 2:
            roman_numeral += 'x' + num_to_roman['I']
        elif digit == 1:
            roman_numeral += 'i' + num_to_roman['I']
        # Update number, removing the last digit
        number = number % 10
    return roman_numeral.lower()

