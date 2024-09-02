
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_numbers = []
    for i in range(a, b+1):
        if str(i)[-1] == "0":
            even_numbers.append(i)
        elif str(i)[-1] == "2":
            even_numbers.append(i)
        elif str(i)[-1] == "4":
            even_numbers.append(i)
        elif str(i)[-1] == "6":
            even_numbers.append(i)
        elif str(i)[-1] == "8":
            even_numbers.append(i)
        elif str(i)[-1] == "":
            even_numbers.append(i)
    return even_numbers

