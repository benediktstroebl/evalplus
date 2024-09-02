
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
    if not 1 <= number <= 1000:
        raise ValueError('Input should be a positive integer between 1 and 1000')
    
    numerals = [('','I'),('','II'),('','III'),('','IV'),('','V'),('','VI'),'VII','VIII','IX',
                ('','X'),('','XI'),('','XII'),('','XIII'),('','XIV'),('','XV'),('','XVI'),'XVII',
                ('','XVIII'),('','XIX'),('','XX'),('','XXI'),('','XXII'),('','XXIII'),('','XXIV'),
                ('','XXV'),('','XXVI'),('','XXVII'),('','XXVIII'),('','XXIX'),('','XXX'),('','XXXI')]

    result = ''
    i = 0
    while number:
        digit = number % 10
        result += numerals[i][1]*digit
        number /= 10
        i += 1
    return result.lower()

