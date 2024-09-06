
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Convert a and b to strings
    a_str = str(a)
    b_str = str(b)
    
    # Split the strings into individual digits
    a_digits = [int(digit) for digit in a_str]
    b_digits = [int(digit) for digit in b_str]
    
    # Iterate through the digits
    for i in range(len(a_digits)):
        # Check if the current digit is even
        if a_digits[i] % 2 == 0:
            # If it is, add it to the result
            result.append(a_digits[i])
        else:
            # If it's not, subtract 1 from the result
            result.append(a_digits[i])
            result.pop()
    
    # Add the last digit (which is always even) to the result
    result.append(b_digits[-1])
    
    return result
