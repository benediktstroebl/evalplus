
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a % 2 == 0:
        even_nums = [a]
    else:
        even_nums = [a+1]
    while even_nums[-1] < b:
        even_nums.append(even_nums[-1] + 2)
    return even_nums

