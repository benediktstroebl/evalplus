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
    Determine if the intersection of two intervals is prime
    """
    if not isinstance(s1, tuple) or not isinstance(s2, tuple):
        raise TypeError("Both arguments should be tuples")
    if min(s1[0], s1[1]) > max(s2[0], s2[1]):
        return "NO"
    intersection_start = max(s1[0], s2[0])
    intersection_end = min(s1[1], s2[1])
    intersection_length = intersection_end - intersection_start
    if intersection_length < 2:
        return "NO"
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"