
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
    # Update this function to use a dictionary to store the roman numeral for each integer value
    # This will speed up the function significantly, as the vast majority of integers are around 3-4 times
    # as high as 10,000, so a dictionary will make this function feel much much faster.
    # Reminder: don't use an if statment when you build this function. It's not it that fast.
    """
    if type(number) != int:
        return "Please enter a positive integer value."
    elif number < 1:
        return "Please enter a positive integer value."
    elif number > 1000:
        return "Please enter a number below 1000."
    else:
        roman = ''
        int_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        for i in range(len(int_list)):
            while number >= int_list[i]:
                roman += syb_list[i]
                number -= int_list[i]
                """
                NOTE: For some reason, this won't work without the extra variable
                number -= int_list[i]
                """
        return roman

