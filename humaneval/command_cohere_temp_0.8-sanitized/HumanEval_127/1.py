def is_prime(n):
    """
    Checks whether a positive integer is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Determine whether the length of the intersection of two closed intervals is prime
    """
    interval_intersection = max(s1[1], s2[1]) - min(s1[0], s2[0])
    if not interval_intersection or not is_prime(interval_intersection):
        return "NO"
    else:
        return "YES"