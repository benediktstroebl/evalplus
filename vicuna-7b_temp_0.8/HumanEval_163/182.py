
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Create a dictionary that maps the digits 0 to 9 to their value
    # when used as a number in Python.
    digits = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9
    }

    # Create a list of integers from a to b
    numbers = [i for i in range(a, b + 1)]

    # Create an empty list to store the even digits
    even_digits = []

    # Loop through the numbers in the list
    for number in numbers:
        # If the number is even, append it to the list of even digits
        if number % 2 == 0:
            even_digits.append(number)

    return even_digits
