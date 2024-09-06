
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

    roman_number = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    
    if 1 <= number <= 1000:
        
        roman_string = ""
        
        for numeral, val in roman_number.items():
            
            roman_string = roman_string + int_to_mini_roman(number // val) * val
            number = number % val
            
        return roman_string.lower()
        
    else:
        
        raise ValueError("Number outside range")
        
