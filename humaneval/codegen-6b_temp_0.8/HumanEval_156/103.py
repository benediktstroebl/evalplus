
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
    
    # Create a dictionary mapping integers to roman numerals
    int_to_roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M'}
    
    # Initialize answer string
    answer_string = ''
    
    # Convert the number to roman numerals
    while number > 0:
        # If the number is in the dictionary, add the matching roman numeral to the answer string
        if number in int_to_roman:
            answer_string += int_to_roman[number]
        
        # Determine the greatest common denominator between the number and the integer
        # that is less than the number and the integer that is the smallest
        # greater than the number.
        greatest_common_divisor = 1
        for divisor in int_to_roman:
            if divisor < number and divisor > greatest_common_divisor:
                greatest_common_divisor = divisor
        
        # Subtract the value of the divisor from the number
        number -= greatest_common_divisor
    
    # Return the answer string in lowercase
    return answer_string.lower()
