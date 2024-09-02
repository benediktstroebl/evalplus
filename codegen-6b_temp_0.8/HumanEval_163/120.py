
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # time complexity: O(log(b - a)) => O(b - a)
    # space complexity: O(log(b - a))
    if a <= b:
        result = []
        while a <= b:
            s = str(a)
            digits = ''.join(digit for digit in s if s.index(digit) % 2 == 0)
            result.append(int(digits))
            a += 1
        return result

