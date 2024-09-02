
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a%2==0 and b%2==0:
        if a>b:
            return [a, a+2, a+4, a+6, a+8]
        else:
            return [b, b-2, b-4, b-6, b-8]
    elif a%2==0 and b%2!=0:
        return []
    elif a%2!=0 and b%2==0:
        return []
    else:
        return [a, a+2, a+4, a+6, a+8]

