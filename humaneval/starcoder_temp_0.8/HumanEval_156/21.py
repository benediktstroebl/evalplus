
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

    def int_to_roman(n):
        """
        Given a positive integer, obtain its roman numeral equivalent as a string,
        and return it in lowercase.
        Restrictions: 1 <= num <= 3999

        Examples:
        >>> int_to_roman(1) == 'i'
        >>> int_to_roman(4) == 'iv'
        >>> int_to_roman(8) == 'viii'
        """

        roman = ''
        while n >= 1000:
            roman += 'M'
            n -= 1000
        while n >= 900:
            roman += 'CM'
            n -= 900
        while n >= 500:
            roman += 'D'
            n -= 500
        while n >= 400:
            roman += 'CD'
            n -= 400
        while n >= 100:
            roman += 'C'
            n -= 100
        while n >= 90:
            roman += 'XC'
            n -= 90
        while n >= 50:
            roman += 'L'
            n -= 50
        while n >= 40:
            roman += 'XL'
            n -= 40
        while n >= 10:
            roman += 'X'
            n -= 10
        while n >= 9:
            roman += 'IX'
            n -= 9
        while n >= 5:
            roman += 'V'
            n -= 5
        while n >= 4:
            roman += 'IV'
            n -= 4
        while n >= 1:
            roman += 'I'
            n -= 1
        return roman

    roman = int_to_roman(number)
    result = ''
    for i in range(len(roman)):
        if i < len(roman) - 1 and roman[i] == roman[i + 1]:
            result += roman[i:i + 2]
        else:
            result += roman[i]
    return result

