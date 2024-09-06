
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

    if not isinstance(number, int) or number < 1 or number > 1000:
        return None

    tens = ['', 'x', 'xx', 'xxx', 'x', 'xx', 'xxx', 'x', 'xx', 'xxx']
    numbers = [None, 'i', 'ii', 'iii', 'v', 'vi', 'vii', 'viii', 'x', 'xi', 'xii']

    result = []

    while number > 0:
        number -= number % 10
        number = number // 10

        result.append(numbers[10 * number])

    return ''.join(result[::-1])
