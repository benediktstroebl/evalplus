def is_prime(n):
    """
    Checks if a number is prime
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
    Determine whether the length of intersection of two given intervals is a prime number or not
    :param s1: (start1, end1)
    :param s2: (start2, end2)
    :return: "YES" or "NO"
    """
    x1, y1 = s1
    x2, y2 = s2
    if x1 > y2 or x2 > y1:
        return "NO"
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 < y2:
        y1, y2 = y2, y1
    if x2 - x1 == 0:
        return "NO"
    return "YES" if is_prime(y2 - y1) else "NO"