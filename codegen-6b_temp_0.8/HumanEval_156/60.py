
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
    if number < 1 or number > 1000:
        raise ValueError("Input out of range")

    roman = ''

    # Since 'LC' comes before 'LI' before 'IV', convert the
    # integer value 'n' into its roman equivalent, which would be
    # 'LC' in the example above and 'L' in the following.
    pow_ten = [1, 10, 100, 1000]
    for val in reversed(pow_ten):
        if number >= val:
            roman += 'L' * (number // val)
            number %= val
    # Next, convert the integer 'n' into its roman equivalent.
    # For example, 'n' is 'IV', '7' is 'VII', '7' is 'VII', and '8' is 'VIII'.
    # In this loop, number equals to '8'.
    val_one = [1, 1, 1, 1]
    val_five = [10, 5, 50, 500]
    val_tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    val_thousands = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    for i in reversed(range(1, len(val_one))):
        if number >= val_one[i]:
            roman += val_thousands[i] + val_tens[number // val_one[i]]
            number %= val_one[i]

    # Finally, convert the integer 'n' into its roman equivalent.
    # For example, 'n' is 'IV', '7' is 'VII', '7' is 'VII', and '8' is 'VIII'.
    # In this loop, number equals to '8'.
    val_one = [1, 1, 1, 1]
    val_five = [5, 10, 50, 500]
    val_tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    val_