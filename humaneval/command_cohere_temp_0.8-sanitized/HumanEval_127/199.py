def is_prime(n):
    """
    Checks if a number is prime
    Args:
        n (int): number to check
    Returns:
        bool: True if n is prime, otherwise False
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Check if the intersection of two intervals is prime
    Args:
        s1 (tuple): first interval tuple (start, end)
        s2 (tuple): second interval tuple (start, end)
    Returns:
        str: "YES" if the intersection is prime, otherwise "NO"
    """
    if not (s1[0] <= s2[1] and s1[1] >= s2[0]):
        return "NO"
    else:
        intersect_start = max(s1[0], s2[0])
        intersect_end = min(s1[1], s2[1])
        intersect_len = intersect_end - intersect_start
        if is_prime(intersect_len):
            return "YES"
        else:
            return "NO"