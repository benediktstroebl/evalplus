
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
    # Check for special case of 1, which maps to I
    if number == 1:
        return 'I'
    # Map 2-39 to A-Z
    mapping = [chr(i + 27 + 97) for i in range(2, 40)]
    # Handle 40-99 by using dictionary
    mapping[40] = 'X'
    mapping[41] = 'XI'
    mapping[42] = 'XII'
    mapping[43] = 'XIII'
    mapping[44] = 'XIV'
    mapping[45] = 'XV'
    mapping[46] = 'XVI'
    mapping[47] = 'XVII'
    mapping[48] = 'XVIII'
    mapping[49] = 'XIX'
    mapping[50] = 'XX'
    mapping[51] = 'XXI'
    mapping[52] = 'XXII'
    mapping[53] = 'XXIII'
    mapping[54] = 'XXIV'
    mapping[55] = 'XXV'
    mapping[56] = 'XXVI'
    mapping[57] = 'XXVII'
    mapping[58] = 'XXVIII'
    mapping[59] = 'XXIX'
    mapping[60] = 'XXX'
    mapping[61] = 'XL'
    mapping[62] = 'L'
    mapping[63] = 'LI'
    mapping[64] = 'LII'
    mapping[65] = 'LIII'
    mapping[66] = 'LIV'
    mapping[67] = 'LV'
    mapping[68] = 'LVI'
    mapping[69] = 'LVII'
    mapping[70] = 'LVIII'
    mapping[71] = 'LIX'
    mapping[72] = 'LX'
    mapping[73] = 'LXI'
    mapping[74] = 'LXII'

    num_lower = [int(
