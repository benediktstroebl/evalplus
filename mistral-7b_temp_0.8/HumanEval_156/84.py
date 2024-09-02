
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
    dict = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    if number in dict:
        return number
    num = str(number)
    if len(num) == 1:
        return dict[num]
    if len(num) == 2:
        num = num[0] + num[1]
        if int(num) >= 10:
            return dict[num]
        if dict[num[1]] > dict[num[0]]:
            return dict[num[0]] + dict[num[1]]
        else:
            return dict[num[1]] - dict[num[0]]
    if len(num) == 3:
        num = num[0] + num[1] + num[2]
        if int(num) >= 100:
            return dict[num]
        if
