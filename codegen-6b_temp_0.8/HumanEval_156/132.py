
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
    if not isinstance(number, int) or not 1 <= number <= 1000:
        raise ValueError('int_to_mini_roman: argument must be a positive integer')
    
    v = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
         '', '', '', '']

    v[1] = 'i'
    v[2] = 'ii'
    v[3] = 'iii'
    v[4] = 'iv'
    v[5] = 'v'
    v[6] = 'vi'
    v[7] = 'vii'
    v[8] = 'viii'
    v[9] = 'ix'
    v[10] = 'x'
    v[11] = 'xi'
    v[12] = 'xii'
    v[13] = 'xiii'
    v[14] = 'xiv'
    v[15] = 'xv'
    v[16] = 'xvi'
    v[17] = 'xvii'
    v[18] = 'xviii'

    v[19] = 'x'
    v[20] = 'xl'
    v[30] = 'xc'
    v[40] = 'xd'
    v[50] = 'xl'
    v[60] = 'xl'
    v[70] = 'xl'
    v[80] = 'xl'
    v[90] = 'xl'

    v[100] = 'c'
    v[200] = 'cc'
    v[300] = 'cc'
    v[400] = 'cc'
    v[500] = 'cc'
    v[600] = 'cc'
    v[700] = 'cc'
    v[800] = 'cc'
    v[900] = 'cc'

    v[1000] = 'm'
    v[2000] = 'mm'
    v[