
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
    mini_roman_numeral_list = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix"]

    roman_numeral_list = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx", "xxi", "xxii", "xxiii", "xxiv", "xxv", "xxvi", "xxvii", "xxviii", "xxix", "xxx", "xxxi", "xxxii", "xxxiii", "xxxiv", "xxxv", "xxxvi", "xxxvii", "xxxviii", "xxxix", "xl", "xli", "xlii", "xliii", "xliv", "xlv", "xlvi", "xlvii", "xlviii", "xlix", "l", "li", "lii", "liii", "liv", "lv", "lvi", "lvii", "lviii", "lix", "lx", "lxi", "lxii", "lxiii", "lxiv", "lxv", "lxvi", "lxvii", "lxviii", "lxix", "lxx", "lxxi", "lxxii", "lxxiii", "lxxiv", "lxxv", "lxxvi", "lxxvii", "lxxviii", "lxxix", "lxxx", "lxxxi", "lxxxii", "lxxxiii", "lxxxiv", "lxxxv", "lxxxvi", "lxxxvii", "lxxxviii", "lxxxix", "xc", "xci", "xcii", "xciii", "xciv", "xcv", "xcvi", "xcvii", "xcviii", "xcix", "c", "ci", "cii", "
