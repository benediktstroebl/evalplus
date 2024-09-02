
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
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    # Go through the dictionary in descending order.
    # If the value of the letter is greater than or equal to the number,
    # add the letter to the result and subtract its value from the number.
    # Else, add 2 * its value to the number and replace the letter by nothing.
    # Continue with the next letter until the number is 0.
    result = ''
    for letter, value in sorted(roman_dict.items(), key=lambda x: x[1], reverse=True):
        while number >= value:
            result += letter
            number -= value
        if number >= 2 * value:
            result += 2 * letter
            number -= 2 * value
    return result.lower()

