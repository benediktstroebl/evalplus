def is_prime(n):
    """
    Checks whether the given integer n is a prime number or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Checks whether the length of the intersection of two given intervals is a prime number or not.
    """
    if s1[0] > s2[1] or s1[1] < s2[0]:
        return "NO"
    s = max(s1[1], s2[1]) - min(s1[0], s2[0])
    if not is_prime(s):
        return "NO"
    return "YES"