def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Determine if the length of the intersection of two closed intervals is prime
    :param s1: (start1, end1)
    :param s2: (start2, end2)
    :return: "YES" if prime, "NO" if not prime or no intersection
    """
    if s1[0] > s2[1] or s2[0] > s1[1]:
        return "NO"
    # intersection is a prime if both start and end are prime
    int_start = max(s1[0], s2[0])
    int_end = min(s1[1], s2[1])
    if is_prime(int_start) and is_prime(int_end):
        return "YES"
    else:
        return "NO"