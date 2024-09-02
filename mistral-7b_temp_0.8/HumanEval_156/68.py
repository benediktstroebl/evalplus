
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
    # Convert the input integer to a list of digits
    digits = [int(num) for num in str(number)]
    digits_roman = []

    # Append the roman numeral equivalent of the digits
    for i in range(len(digits)):
        if i == 0:
            digits_roman.append(str(digits[i]))
        elif i == 1:
            if digits[i] == 1:
                digits_roman.append("i")
            elif digits[i] == 2:
                digits_roman.append("ii")
            elif digits[i] == 3:
                digits_roman.append("iii")
            elif digits[i] == 4:
                digits_roman.append("iv")
            elif digits[i] == 5:
                digits_roman.append("v")
            elif digits[i] == 6:
                digits_roman.append("vi")
            elif digits[i] ==
