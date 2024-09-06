
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
    assert 0 < number < MAX_NUMBER, 'number must be between 1 and 1000'

    if number == 1:
        return 'i'
    
    prev_num = number / 10
    prev_num_str = int_to_mini_roman(prev_num)

    num_str = ''
    if number <= 5:
        num_str += 'v' * (number - 1)
    else:
        num_str += 'v' + prev_num_str
        num_str += (5 - prev_num) * 'i'

    return num_str.lower()
