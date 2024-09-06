def is_prime(n):
    """
    Checks whether a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Determine whether the length of the intersection of two closed intervals is prime
    """
    if not ((s1[0] >= s2[0]) and (s1[1] <= s2[1])) and not ((s2[0] >= s1[0]) and (s2[1] <= s1[1])):
        return "NO"
    else:
        overlap = max(s1[0], s2[0]) - min(s1[1], s2[1])
        if is_prime(overlap):
            return "YES"
        else:
            return "NO"