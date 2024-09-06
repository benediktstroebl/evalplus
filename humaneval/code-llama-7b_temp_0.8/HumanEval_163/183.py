
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Base Case:
    # If one of the numbers is even and the other is odd, return an empty list.
    if a % 2 != 0 or b % 2 != 0:
        return []
    # If one number is smaller than the other, swap them.
    if a < b:
        a, b = b, a
    # Create an empty list to store even numbers.
    even_numbers = []
    # Loop through all the numbers.
    for number in range(a, b + 1):
        # If the number is even, add it to the list.
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

