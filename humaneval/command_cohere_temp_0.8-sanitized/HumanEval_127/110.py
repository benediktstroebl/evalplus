def is_prime(n):
    """
    Checks if a number is prime

    Args:
        n (int): Number to check if it's prime

    Returns:
        bool: True if n is prime, otherwise False
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def intersection(s1, s2):
    """
    Check if the intersection of two intervals is prime

    Args:
        s1 (tuple): First interval (start, end)
        s2 (tuple): Second interval (start, end)

    Returns:
        str: "YES" if the intersection is prime, otherwise "NO"
    """
    if max(s1[0], s1[1]) > min(s2[0], s2[1]) or max(s2[0], s2[1]) > min(s1[0], s1[1]):
        return "NO"
    else:
        intersection_length = (max(s1[0], s2[0]) + min(s1[1], s2[1])) // 2
        if is_prime(intersection_length):
            return "YES"
        else:
            return "NO"