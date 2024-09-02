
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

    roman = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
    integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    answer = ''
    for i in range(len(integer)):
        answer += roman[integer[i]] * (number // integer[i])
        number %= integer[i]
    return answer.lower()
