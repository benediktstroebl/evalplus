
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Create a list of integers from a to b
    list_of_integers = [i for i in range(a, b+1)]

    # Initialize an empty list to store even digits
    even_digits = []

    # Iterate through the list of integers
    for i in list_of_integers:
        # If the current integer is even, append it to the list of even digits
        if i % 2 == 0:
            even_digits.append(i)

    # Return the list of even digits
    return even_digits
