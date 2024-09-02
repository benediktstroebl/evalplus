
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
    # note: number is assumed to be an integer, but no exception is raised
    #       if the number is not an integer
    #       if it is not an integer (i.e., an exception is raised), then the
    #       program is stopped and an error message is printed
    #
    # note: we could make some assumptions on the lengths of the numbers
    #       and account for them...
    #

    # convert to letters
    letters = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    roman = ""
    while number > 0:
        # determine the value of the remander
        remander = (number - (number // 10 * 10))
        # depending on the remander, add it to the roman numeral
        if(2 <= remander and remander <= 10):
            roman = letters[remander] + roman
        elif(remander == 1):
            roman = letters[remander] + roman
        else:
            roman = roman + letters[remander]
        number = number // 10
    return roman

