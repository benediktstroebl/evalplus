
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    ans = []
    while a <= b:
        if a % 2 != 0:
            ans.append(a)
        a += 1
    return ans

assert generate_integers(2, 8) == [2, 4, 6, 8]
assert generate_integers(8, 2) == [2, 4, 6, 8]
assert generate_integers(10, 14) == []
