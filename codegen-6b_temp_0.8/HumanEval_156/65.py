
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
    if not isinstance(number, int) or not 1 <= number <= 1000:
        raise ValueError

    # Initialize the answer to the empty string
    result = ""

    # Dict to store the number of roman numerals of each type
    roman_numerals = {1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v',
                      6: 'vi', 7: 'vii', 8: 'viii', 9: 'ix'}

    roman = ('m', 'c', 'd', 'cm', 'cd', 'xc', 'xl', 'x', 'ix', 'v', 'vi',
             'vii', 'viii', 'ix')

    # Loop over the number of digits of number
    for i in range(len(str(number))):
        digit = number % 10
        number = number // 10

        # If we have a 4 digit number
        if digit == 4:
            # Get the next digit after the 4th digit
            digit = number % 10
            # If the next digit is 5 or 7
            if digit == 5 or digit == 7:
                result = roman[i] + roman_numerals[4] + result
            # If the next digit is in the dictionary
            elif roman_numerals.get(digit):
                # Get the next letter corresponding to the roman numeral
                result = roman_numerals[digit] + result
            # If the next digit is a 1
            elif digit == 1:
                # Get the next letter corresponding to the roman numeral
                result = roman[i] + roman_numerals[7] + result
            # If the next digit is greater than 5
            elif digit > 5:
                # Add the roman numeral correspondig to the digit
                result = roman[i] + roman_numerals[5] + result
            # If the next digit is not in the dictionary
            else:
                # Add the roman numeral correspondig to the digit
                result = roman[i] + roman_numerals[digit] + result
        # If we have a 3 digit number
        elif digit