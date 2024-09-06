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
    Check if the intersection of two intervals is a prime number
    """
    if s1[0] > s2[1] or s1[1] < s2[0]:
        return "NO"
    interval_length = max(s1[1], s2[1]) - min(s1[0], s2[0])
    if not is_prime(interval_length):
        return "NO"
    return "YES"