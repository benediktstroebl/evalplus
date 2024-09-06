def is_prime(n):
    """
    Checks if a number is prime
    Args:
        n (int): number to check
    Returns:
        bool: whether n is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Determine whether the length of intersection of two given closed intervals is a prime number.
    Args:
        s1 (tuple): first interval, interval = (start, end)
        s2 (tuple): second interval, interval = (start, end)
    Returns:
        str: "YES" if the length of the intersection is a prime number, otherwise "NO"
    """
    x1, y1 = s1
    x2, y2 = s2
    if x1 > y2 or x2 > y1:
        return "NO"
    else:
        intersection_start = max(x1, x2)
        intersection_end = min(y1, y2)
        intersection_length = intersection_end - intersection_start
        if is_prime(intersection_length):
            return "YES"
        else:
            return "NO"