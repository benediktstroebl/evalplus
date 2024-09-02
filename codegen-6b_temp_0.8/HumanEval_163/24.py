
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    generator = range(a, b + 1)
    if a % 2 == 0:
        even_nums = [num for num in generator if num % 2 == 0]
        odd_nums = [num for num in generator if num % 2 != 0]
        return even_nums + odd_nums
    else:
        return [num for num in generator if num % 2 != 0]

