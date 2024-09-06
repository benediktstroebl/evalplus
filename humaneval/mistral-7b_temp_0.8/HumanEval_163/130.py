
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # Write your code here

    # While a is less than b
    while a < b:
        if a % 2 == 0:
            # Append a to list
            list.append(a)
        # Add 2 to a
        a += 2
    return list

