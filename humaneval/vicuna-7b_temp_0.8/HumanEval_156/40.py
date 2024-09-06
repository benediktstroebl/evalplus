
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
    roman_numerals = {'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500'}

    numeral = str(number)
    symbol = numeral[0]
    for i in range(1, len(numeral)):
        numeral_value = int(numeral[i:i+1])
        if numeral_value > 1000:
            break
        numeral = numeral[:i] + roman_numerals[symbol] + numeral[i+1:]
        symbol = numeral[0]
    return numeral.lower()
