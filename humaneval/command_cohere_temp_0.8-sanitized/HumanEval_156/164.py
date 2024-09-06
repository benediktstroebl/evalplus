def int_to_mini_roman(n):
    if n < 1:
        return ""

    res = []
    for curr_v, roman_numeral in enumerate(ROMAN_NUMERALS, 1):
        while n >= curr_v:
            res.append(roman_numeral)
            n -= curr_v

    return ''.join(res)
ROMAN_NUMERALS = 'iixvxlcdm'