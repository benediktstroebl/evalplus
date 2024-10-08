def int_to_mini_roman(number):
    # Define the mapping from integers to roman numerals
    roman_nums = {
        1000: 'm',
        900: 'cm',
        500: 'd',
        400: 'cd',
        100: 'c',
        90: 'xc',
        50: 'l',
        40: 'xl',
        10: 'x',
        9: 'ix',
        5: 'v',
        4: 'iv',
        1: 'i'
    }
    # Check if the input number is within the allowed range
    if number < 1 or number > 1000:
        raise ValueError('Number must be between 1 and 1000')
    # Convert the number to roman numerals
    result = ''
    for value, numeral in roman_nums.items():
        while number >= value:
            result += numeral
            number -= value
    return result.lower()
