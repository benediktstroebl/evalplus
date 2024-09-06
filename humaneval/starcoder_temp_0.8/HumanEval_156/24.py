
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

    # Roman numbers less than 5000 are not supported.
    if number <= 0 or number >= 5000:
        return None

    # Get the number of times 1000 is divisible.
    divisors = int(number / 1000)
    # The number of times 1000 is not divisible is equal to the number of
    # times 100 is divisible by 10.
    # This ensures that 'MMMM' and 'MMM' is not returned, for instance.
    not_divisors = int((number % 1000) / 100)
    # The number of times 100 is not divisible is equal to the number of times
    # 10 is divisible by 10.
    # This ensures that 'XXX' and 'XX' is not returned, for instance.
    not_divisors += int((number % 100) / 10)
    # The number of times 10 is not divisible is equal to the number of times
    # 1 is divisible by 10.
    # This ensures that 'V' and 'X' is not returned, for instance.
    not_divisors += int((number % 10))

    # Start with 1000.
    roman = 'M' * divisors
    # Add 900, 800,..., 100.
    roman += 'C' * not_divisors

    # Subtract 900, 800,..., 100.
    number -= 100 * not_divisors
    # Get the number of times 100 is divisible.
    divisors = int(number / 100)
    # The number of times 100 is not divisible is equal to the number of times
    # 10 is divisible by 10.
    # This ensures that 'CM' and 'C' is not returned, for instance.
    not_divisors = int((number % 100) / 10)
    # The number of times 10 is not divisible is equal to the number of times
    # 1 is divisible by 10.
    # This ensures that 'IX' and '
