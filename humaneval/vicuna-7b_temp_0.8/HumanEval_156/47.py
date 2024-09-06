
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
    # Handle cases 1000-900
    if number >= 1000 and number <= 900:
        return f'{number}'
    # Handle cases 900-800
    elif number >= 800 and number <= 899:
        return f'{number}c'
    # Handle cases 800-700
    elif number >= 700 and number <= 799:
        return f'{number}x'
    # Handle cases 700-600
    elif number >= 600 and number <= 699:
        return f'{number}xi'
    # Handle cases 600-500
    elif number >= 500 and number <= 599:
        return f'{number}lx'
    # Handle cases 500-400
    elif number >= 400 and number <= 499:
        return f'{number}xl'
    # Handle cases 400-300
    elif number >= 300 and number <= 399:
        return f'{number}xxxvii'
    # Handle cases 300-200
    elif number >= 200 and number <= 299:
        return f'{number}xciii'
    # Handle cases 200-100
    elif number >= 100 and number <= 199:
        return f'{number}cxxxix'
    # Handle cases 100-90
    elif number >= 90 and number <= 99:
        return f'{number}xcviii'
    # Handle cases 90-80
    elif number >= 80 and number <= 89:
        return f'{number}xlviii'
    # Handle cases 80-70
    elif number >= 70 and number <= 79:
        return f'{number}xlvii'
    # Handle cases 70-60
    elif number >= 60 and number <= 69:
        return f'
