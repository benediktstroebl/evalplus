def is_prime(n):
    """
    Checks whether a positive integer 'n' is a prime number or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Determine whether the length of the intersection of two given closed intervals is a prime number or not.
    """
    x1, y1 = s1
    x2, y2 = s2
    if x1 > y2 or x2 > y1:
        return "NO"
    else:
        dx = max(x2, x1) - min(x2, x1)
        dy = max(y2, y1) - min(y2, y1)
        if is_prime(dx):
            return "YES"
        elif is_prime(dy):
            return "YES"
        else:
            return "NO"