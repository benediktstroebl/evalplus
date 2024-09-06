
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
    return ''.join(
        (
            (
                'I'
                if number in {1, 5, 10}
                else (
                    'V'
                    if number == 50 else 'X'
                )
            ),
            *(
                map(
                    lambda x: '',
                    range(
                        number // 10 ** i * 10 ** (i + 1),
                        number,
                        -10 ** i
                    )
                )
            )
        )
    )
