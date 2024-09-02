
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    
    # even_digits is a list of all the even numbers between a and b
    # in ascending order.
    even_digits = []

    # num is the current integer to be added to even_digits
    num = a
    
    # while num is between a and b, add the current even number to
    # even_digits.
    while num <= b:
        if num % 2 == 0:
            even_digits.append(num)
        num += 1

    return even_digits
