
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    numbers = []
    if a % 2 == 0:
        numbers.append(a)
    if b % 2 == 0:
        numbers.append(b)
    if len(numbers) == 0:
        return []
    for num in range(numbers[0] + 1, numbers[1] + 1, 2):
        numbers.append(num)
    return numbers

