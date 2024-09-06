
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
    roman_chars = 'IVXLCDM'

    def to_roman(num):
        result = ''
        while num > 0:
            if num % 1000 == 4:
                result = 'C' + result
            elif num % 1000 == 3:
                result = 'D' + result
            elif num % 1000 == 2:
                result = 'E' + result
            elif num % 1000 == 1:
                result = 'X' + result
            num //= 1000
            if num > 0:
                num %= 1000
                if num == 0:
                    result += 'D'
                elif num == 1:
                    result += 'V'
                elif num == 2:
                    result += 'I'
                elif num == 3:
                    result += 'V'
                elif num == 4:
                    result += 'I'
                elif num == 5:
                    result += 'V'
                elif num == 6:
                    result += 'X'
                elif num == 7:
                    result += 'L'
                elif num == 8:
                    result += 'L'
                elif num == 9:
                    result += 'X'
            else:
                result += '0'
        return result

    return ''.join(roman_chars[i] for i in (to_roman(number)))
