
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        return []
    elif a == b:
        return [a]
    else:
        even_digits = []
        for num in range(a, b+1):
            digits = str(num)
            even_digits.append(digits[0])
            if digits[1] in ['0', '1']:
                even_digits.append(digits[1])
        return even_digits