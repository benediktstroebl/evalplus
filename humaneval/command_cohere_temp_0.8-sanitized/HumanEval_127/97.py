def is_prime(n):
    """
    Checks if a number is prime

    Args:
        n (int): Number to check if prime

    Returns:
        bool: True if n is prime, otherwise False
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Check if the intersection of two intervals is a prime number

    Args:
        s1 (tuple): First interval (start, end)
        s2 (tuple): Second interval (start, end)

    Returns:
        str: "YES" if the intersection is prime, otherwise "NO"
    """
    if max(s1[0], s1[1]) > min(s2[0], s2[1]) or max(s2[0], s2[1]) > min(s1[0], s1[1]):
        return "NO"
    else:
        interval_length = max(s1[1], s2[1]) - min(s1[0], s2[0])
        if is_prime(interval_length):
            return "YES"
        else:
            return "NO"