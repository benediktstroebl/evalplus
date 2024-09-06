
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
    roman_letters = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    letter_list = []
    roman = ""

    number = int(number)
    while number > 0:
        for letter, value in roman_letters.items():
            if number >= value:
                number -= value
                letter_list.append(letter)
                break

    for i in range(len(letter_list) - 1):
        if roman_letters[letter_list[i + 1]] > roman_letters[letter_list[i]]:
            roman += letter_list[i + 1] + letter_list[i]
        else:
            roman += letter_list[i]

    roman += letter_list[-1]
    return roman



