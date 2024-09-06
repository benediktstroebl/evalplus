
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
    roman_numerals = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii",
                      "ix", "x", "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii",
                      "xviii", "xix", "xx", "xxx", "xl", "l", "li", "lii", "liii",
                      "liv", "lx", "lxi", "lxii", "lxiii", "lxiv", "lxv", "lxvi",
                      "lxvii", "lxviii", "lxix", "lxx", "lxxi", "lxxii", "lxxiii",
                      "lxxiv", "lxxv", "lxxvi", "lxxvii", "lxxviii", "lxxix", "lxxx",
                      "lxxxi", "lxxxii", "lxxxiii", "lxxxiv", "lxxxv", "lxxxvi",
                      "lxxxvii", "lxxxviii", "lxxxix", "xc", "c", "ci", "cii", "ciii",
                      "ciiv", "cv", "cvi", "cvii", "cviii", "cix", "cx", "cxi", "cxii",
                      "cxiii", "cxiv", "cxv", "cxvi", "cxvii", "cxviii", "cxix", "cxx",
                      "cxxi", "cxxii", "cxxiii", "cxxiv", "cxxv", "cxxvi", "cxxvii",
                      "cxxviii", "cxxix", "cxxx", "cxxxi", "cxxxii", "cxxxiii", "cxxxiv",
                      "cxxxv", "cxxxvi", "cxxxvii", "cxxxviii", "cxxxix", "cxl", "cl",
                      "cli", "clii", "cliii", "cliv", "clv", "clvi", "clvii", "clviii",
                      "clx", "clxi", "clxii", "clxiii", "clxiv", "clxv", "clxvi", "clxvii",
                      "clxviii
