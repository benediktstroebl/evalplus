
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Start with a and b as the first and last digits
    digits = [a, b]
    # Generate digits by iteratively taking the midpoint of the two digits
    # and adding 1 to the tens digit, effectively swapping the tens and ones
    # digits
    for i in range(1, max(a, b) + 1):
        if (a // i) * 10 + (a // i + 1) == b:
            digits.append((a // i) * 10 + 1)
            a //= i
        else:
            digits.append(a)
            break
    return digits
