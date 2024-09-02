
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
    thousands = number // 1000
    hundreds = (number - 1000 * thousands) // 100
    tens = (number - 1000 * thousands - 100 * hundreds) // 10
    units = (number - 1000 * thousands - 100 * hundreds - 10 * tens)

    answer = ""

    if hundreds >= 5:
        answer += "d"
        hundreds -= 5
    if hundreds == 4:
        answer += "cd"
        hundreds -= 4
    if hundreds >= 4:
        answer += "xc"
        hundreds -= 4
    if hundreds == 3:
        answer += "xx"
        hundreds -= 3
    if hundreds >= 3:
        answer += "xx"
        hundreds -= 3
    if hundreds == 2:
        answer += "x"
        hundreds -= 2
    if hundreds == 1:
        answer += "i"
        hundreds -= 1
    if hundreds >= 1:
        answer += "c"
        hundreds -= 1

    if tens == 9:
        answer += "ix"
        tens -= 9
    if tens >= 5:
        answer += "v"
        tens -= 5
    if tens == 4:
        answer += "iv"
        tens -= 4
    if tens == 3:
        answer += "i"
        tens -= 3
    if tens == 2:
        answer += "i"
        tens -= 2
    if tens == 1:
        answer += "i"
        tens -= 1

    if tens >= 1:
        answer += "x"
        tens -= 1

    if units >= 5:
        answer += "v"
        units -= 5
    if units == 4:
        answer += "iv"
        units -= 4
    if units == 3:
        answer += "i"
        units -= 3
    if units == 2:
        answer += "i"
        units -= 2
    if units == 1:
        answer += "i"
        units -=
