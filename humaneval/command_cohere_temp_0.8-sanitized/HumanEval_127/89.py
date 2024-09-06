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
    Determine if the intersection of two intervals is a prime number
    """
    interval = [max(s1[0], s2[0]), min(s1[1], s2[1])]
    if len(interval) == 0:
        return "NO"
    else:
        if is_prime(len(interval)):
            return "YES"
        else:
            return "NO"