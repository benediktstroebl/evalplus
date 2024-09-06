def is_prime(n):
    """
    Checks whether a number is prime
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
    Checks whether the intersection of two intervals is prime
    """
    if s1[0] > s2[1] or s1[1] < s2[0]:
        return "NO"
    inter_start = max(s1[0], s2[0])
    inter_end = min(s1[1], s2[1])
    intersection_length = inter_end - inter_start
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"