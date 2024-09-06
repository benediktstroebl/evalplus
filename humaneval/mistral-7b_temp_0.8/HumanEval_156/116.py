
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

    mini_roman = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]

    roman = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx"]

    hundred = ["c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "cm"]

    thousand = ["m", "mm", "mmm"]

    if number >= 1000:
        return thousand[number // 1000]
    elif number >= 900:
        return thousand[9] + hundred[number % 1000 // 100]
    elif number >= 500:
        return thousand[5] + hundred[number % 500 // 100]
    
