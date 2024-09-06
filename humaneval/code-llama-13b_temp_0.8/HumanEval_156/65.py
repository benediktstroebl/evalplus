
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
    def mini_roman(num):
        if num >= 1000:
            return 'm' + roman(num-1000)
        if num >= 900:
            return 'cm' + roman(num-900)
        if num >= 500:
            return 'd' + roman(num-500)
        if num >= 400:
            return 'cd' + roman(num-400)
        if num >= 100:
            return 'c' + roman(num-100)
        if num >= 90:
            return 'xc' + roman(num-90)
        if num >= 50:
            return 'l' + roman(num-50)
        if num >= 40:
            return 'xl' + roman(num-40)
        if num >= 10:
            return 'x' + roman(num-10)
        if num >= 9:
            return 'ix' + roman(num-9)
        if num >= 5:
            return 'v' + roman(num-5)
        if num >= 4:
            return 'iv' + roman(num-4)
        if num >= 1:
            return 'i' + roman(num-1)
        return ''

    return mini_roman(number).lower()
