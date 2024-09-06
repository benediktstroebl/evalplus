
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
    mini_roman = [ '', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii',
                   'ix', 'x' ]

    assert 1 <= number <= 1000, 'Value not in range'

    # Convert a given number of roman numerals to roman numerals
    def get_roman(n):
        """
        Get the corresponding roman numeral given a number of roman numerals.
        """
        return mini_roman[n]

    # Convert from roman numerals to numerical roman numerals,
    # and append to string in reverse order
    def append_roman(n):
        """
        Append the roman numeral to the string, with the numerals in reverse
        order.
        """
        return get_roman(n) + num_string[-1]

    # Convert a given number of numerical roman numerals to roman numerals
    def get_num(n):
        """
        Get the corresponding roman numeral given a number of roman numerals.
        """
        return mini_roman[int(n)]

    # Convert from roman numerals to numerical roman numerals,
    # and append to string
    def append_num(n):
        """
        Append the roman numeral to the string, preserving the numerals in
        reverse order.
        """
        return num_string[-1] + get_num(n)

    # Convert a given number of roman numerals to roman numerals,
    # and append them to the string in reverse order
    def append_num_roman(n):
        """
        Append the roman numeral to the string, with the numerals in reverse
        order.
        """
        return num_string[-1] + get_roman(n)

    # Loop through each number of roman numerals, ending when the number of
    # numerals is less than the given number.
    for i in range(len(mini_roman), number, -1):
        num_string.append(get_roman(i))

    return ''.join(num_string[::-1])

