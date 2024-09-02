
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # check if a and b are valid inputs
    if a < b:
        raise ValueError("Invalid input: a must be greater than b")
    
    # initialize a list to store the even digits
    digits = []
    
    # iterate through the range a to b
    for i in range(a, b+1):
        # get the digits of the number
        digits_str = str(i)
        
        # remove all the odd digits
        digits_str = digits_str.lstrip("0")
        
        # append the even digits to the list
        digits.append(digits_str)
    
    return digits
