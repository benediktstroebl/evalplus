
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
    roman_dict = {1: "i", 2: "ii", 3: "iii", 4: "iv", 5: "v", 6: "vi",
                  7: "vii", 8: "viii", 9: "ix", 10: "x",
                  20: "x", 30: "xxx", 40: "x", 50: "l",
                  60: "l", 70: "lxxx", 80: "l", 90: "xc",
                  100: "c", 200: "c", 300: "ccc", 400: "cd",
                  500: "d", 600: "d", 700: "dccc", 800: "d",
                  900: "cm", 1000: "m"}

    res = ""
    for num in reversed(range(1, 1000)):
        if number < num:
            break
