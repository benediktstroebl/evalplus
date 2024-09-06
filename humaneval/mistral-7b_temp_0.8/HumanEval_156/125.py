
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
    if number < 1 or number > 1000:
        raise ValueError(
            "Incorrect Input: number must be positive integer greater than 0 and less than 1000")
    # Write your code here
    # hints:
    # 1. you can write a recursive function for this
    # 2. you can use a dictionary for this
    # 3. use the modulus operator to find the last digit of a number
    # 4. use the division operator to remove the last digit of a number
    # 5. use the floor division operator to divide a number by 10

    # return "i" * number
    return ""
