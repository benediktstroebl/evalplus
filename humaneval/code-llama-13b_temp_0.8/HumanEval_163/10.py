
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_list = []
    for x in range(a, b + 1):
        string = str(x)
        for char in string:
            if char.isdigit() and int(char) % 2 == 0:
                even_list.append(int(char))
    return sorted(list(set(even_list)))

