
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
    numeral = str(number)
    roman = ""
    for i in range(len(numeral)):
        if numeral[i] >= "A":
            roman += "".join([numeral[i], "MCMXCVII"[numeral[i - 1] - 'A']])
        elif numeral[i] >= "B":
            roman += "".join([numeral[i], "MCCMXCVII"[numeral[i - 1] - 'B']])
        elif numeral[i] >= "C":
            roman += "".join([numeral[i], "MCMXCVII"[numeral[i - 1] - 'C']])
        else:
            roman += "".join([numeral[i], "M" + str(numeral[i - 1])])
    return roman.lower()
