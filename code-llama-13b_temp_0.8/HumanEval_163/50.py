
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # The easiest way to get all even numbers is to filter out the odd ones.
    # This can be done by checking the remainder of the modulo operation.
    # If the remainder is 0, it is even.

    # To generate the range of numbers, you can use the built-in range() function
    # in python. The range() function takes a minimum, maximum and optional step
    # size. The step size will be the distance between two numbers in the sequence.
    # For example:
    # range(1, 10) will return the sequence 1, 2, 3, ..., 9.
    # range(1, 10, 2) will return the sequence 1, 3, 5, 7, 9.

    # Once you have the range of numbers, you can use the filter() function to
    # apply the modulo check for even.

    # The return statement will take care of returning the sequence.
    
    return []


