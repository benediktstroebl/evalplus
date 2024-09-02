
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    low, high = a, b
    while low < high:
        mid = (low + high) // 2
        if mid - low % 2 != (high - mid) % 2:
            break
        low, high = mid, mid + 2
    return [low] + list(range(mid, high + 1))
