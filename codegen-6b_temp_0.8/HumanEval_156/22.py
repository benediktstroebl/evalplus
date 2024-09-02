
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
    # Initialize a dictionary which maps the ints to their roman equivalent
    # and place these in lowercase.
    NUMBERS_DICT = {1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v', 6: 'vi', 7: 'vii', 8: 'viii', 9: 'ix', 10: 'x',
                    20: 'xl', 30: 'xlxx', 40: 'xlv', 50: 'l', 60: 'lx', 70: 'lxx', 80: 'lf', 90: 'lfx',
                    100: 'c', 200: 'cc', 300: 'ccc', 400: 'cd', 500: 'd', 600: 'dxc', 700: 'dc', 800: 'dcc',
                    900: 'dccc', 1000: 'm', 2000: 'mm', 3000: 'mcm', 4000: 'mcd', 5000: 'dmd',
                    6000: 'dm', 7000: 'dmm', 8000: 'dcm', 9000: 'dmmm', 10000: 'mmcm', 20000: 'mmdd',
                    30000: 'mmdxc', 40000: 'mmdc', 50000: 'mmmmm', 60000: 'mmdcc', 70000: 'mmdCCC',
                    80000: 'mmdCC', 90000: 'mmdCCC', 100000: 'mcmcm', 200000: 'mcmcd', 300000: 'mcmcdc',
                    400002: 'mcmcdCC', 500002: 'mcmdC', 600002: 'mcmdc', 700002: 'mcmdCC',
                    800002: 'mcmdcC', 900002: 'mcmdcCCC', 1000002: 'mcmdCCCC', 2000002: 'mcdcdC',
                    3000002: 'mcdcdCC', 400002: 'mcdcdCC', 500002: 'mcdcdCCC', 600002: 'mcdcdCCCC',
                    700002: 'mcdccC', 800002: 'mcdccCC', 900002: 'mcdccCCC', 1000002: 'mcmdCCCC',
                    2000002: 'md