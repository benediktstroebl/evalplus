def is_prime(n):
    """
    Checks whether a positive integer 'n' is a prime number or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Checks whether the length of the intersection of two given intervals is a prime number or not.
    """
    x = min(s1[1], s2[1]) - max(s1[0], s2[0])
    if x < 0 or not is_prime(x):
        return "NO"
    else:
        return "YES"