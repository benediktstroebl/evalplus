
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
    # Define dictionary of integers corresponding to roman numerals
    roman_numeral_convert = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
                             50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',
                             900: 'CM', 1000: 'M'}

    # If the number is out of range, then return None
    if number > 1000 or number < 1:
        return None

    # Initialize variables for list of strings to be returned and an empty string
    output_list = []
    roman_numeral = ''

    # Calculate number of times to divide by 100
    divide_by = int(number / 100)

    # Traverse through the list of roman numerals
    for i in range(0, divide_by):
        # If the value is 1000, then IX
        if i*100 == number:
            roman_numeral = roman_numeral_convert[1000]
            break
        # If not 1000, for 10, 100 and 400, add the value to the string
        # Separate them and append to list
        elif i*100 < number:
            output_list.append(roman_numeral_convert[100 * (i + 1)])
            output_list.append(roman_numeral_convert[100 * i])

    # Append the remainder to the end of the list
    output_list.append(roman_numeral_convert[number % 100])

    # For each string in the list, append it to the output
    for s in output_list:
        roman_numeral += s

    # Return the roman numeral as a string
    return roman_numeral

