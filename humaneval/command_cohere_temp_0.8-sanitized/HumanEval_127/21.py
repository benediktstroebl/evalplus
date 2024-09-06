def is_prime(n):
    """
    Checks whether a number is prime

    Args:
        n (int): Number to check
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Check whether the intersection of two intervals is prime

    Args:
        s1 (tuple): First interval (start, end)
        s2 (tuple): Second interval (start, end)

    Returns:
        str: "YES" if intersection is prime, "NO" if not
    """
    if not s1 or not s2:
        return "NO"
    int_size = max(0, min(s1[1], s2[1]) - max(s1[0], s2[0]) + 1)
    if int_size == 0:
        return "NO"
    if is_prime(int_size):
        return "YES"
    return "NO"