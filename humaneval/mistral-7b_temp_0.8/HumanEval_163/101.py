
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    list_of_numbers = []
    if a % 2 != 0:
        a = a + 1
    while a < b:
        if a % 2 == 0:
            list_of_numbers.append(a)
            a = a + 1
        else:
            a = a + 1
    if len(list_of_numbers) == 0:
        return list_of_numbers
    else:
        return list_of_numbers
