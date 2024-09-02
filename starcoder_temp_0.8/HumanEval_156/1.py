
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
    # 1. Get all the number of roman numbers in the thousands place.
    # 2. Translate the numeral system to mini-roman.
    # 3. Invert the mini-roman number.
    # 4. Swap the places of the 'i' and 'v' in the inverted mini-roman number.
    # 5. Convert the inverted mini-roman number to the number in the thousands place.
    # 6. Return the number in the thousands place.

    # Get the number of roman numbers in the thousands place.
    num_of_thousands = number // 1000

    # Translate the numeral system to mini-roman.
    mini_roman = number % 1000
    if mini_roman >= 500:
        mini_roman = 500 - mini_roman
        num_of_thousands += 1
    if mini_roman >= 400:
        mini_roman = 400 - mini_roman
    if mini_roman >= 100:
        mini_roman = mini_roman - 100
        mini_roman = 'c' + int_to_mini_roman(mini_roman)
    if mini_roman >= 90:
        mini_roman = mini_roman - 90
        mini_roman = 'xc' + int_to_mini_roman(mini_roman)
    if mini_roman >= 50:
        mini_roman = mini_roman - 50
        mini_roman = 'l' + int_to_mini_roman(mini_roman)
    if mini_roman >= 40:
        mini_roman = mini_roman - 40
        mini_roman = 'xl' + int_to_mini_roman(mini_roman)
    if mini_roman >= 10:
        mini_roman = mini_roman - 10
        mini_roman = 'x' + int_to_mini_roman(mini_roman)
    if mini_roman >= 9:
        mini_roman = mini_roman - 9
        mini_roman = 'ix' + int_to_mini_roman(mini_roman)
    if mini_roman >= 5:
        mini_roman = mini_roman - 5
        mini_roman = 'v' + int_to_mini_roman(
