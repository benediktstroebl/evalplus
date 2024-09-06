
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
    # initialization
    romans = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '']
    numerals = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    chunks = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def convert_to_int(numeral, i):
        """
        Given a string containing a roman numeral, returns the numeral as an
        integer.
        Restrictions: numeral must be a string of Roman numeral characters.
        """
        roman_value = 0

        for char, numeral_value in chunks:
            if numeral.startswith(numeral_value):
                roman_value += char * (numeral.count(numeral_value) - 1)
                numeral = numeral.replace(numeral_value, '', 1)
        return roman_value + numeral_value

    def convert_to_roman(int_val):
        """
        Given an integer, returns its Roman numeral equivalent.
        Restrictions: int_val >= 1
        """
        numeral = ''
        i = 0
        while int_val > 0:
            for value, roman in chunks:
                while int_val >= value:
                    int_val -= value
                    numeral += roman
        return numeral

    # convert to integer
    int_val = convert_to_int(''.join(reversed(str(number))))

    # convert to roman
    roman_numeral = convert_to_roman(int_val)
    # convert to lowercase
    return roman_numeral