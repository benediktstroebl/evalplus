
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
    seen = []
    # The following will handle numbers between 1 and 3999
    # and numbers between 1000 and 3999 as well
    for x in range(1, 400):
        if int(number / x) == 0:
            seen.append(str(x))
        elif int(number / x) == 1:
            seen.append(str(x) + 'i')
        elif int(number / x) == 2:
            seen.append(str(x) + 'ii')
        elif int(number / x) == 3:
            seen.append(str(x) + 'iii')
        elif int(number / x) == 4:
            seen.append(str(x) + 'iv')
        elif int(number / x) == 5:
            seen.append(str(x) + 'v')
        elif int(number / x) == 6:
            seen.append(str(x) + 'vi')
        elif int(number / x) == 7:
            seen.append(str(x) + 'vii')
        elif int(number / x) == 8:
            seen.append(str(x) + 'viii')
        elif int(number / x) == 9:
            seen.append(str(x) + 'ix')
        elif int(number / x) == 10:
            seen.append(str(x) + 'x')
        elif int(number / x) == 11:
            seen.append(str(x) + 'xi')
        elif int(number / x) == 12:
            seen.append(str(x) + 'xii')
        elif int(number / x) == 13:
            seen.append(str(x) + 'xiii')
        elif int(number / x) == 14:
            seen.append(str(x) + 'xiv')
        elif int(number / x) == 15:
            seen.append(str(x) + 'xv')
        elif int(number / x) == 16:
            seen.append(str(x) + 'xvi')
        elif int(number / x) ==