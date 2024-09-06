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
    Determine if the intersection of two intervals is a prime number
    """
    start = max(s1[0], s2[0])
    end = min(s1[1], s2[1])
    if end < start:
        return "NO"
    length = end - start + 1
    if is_prime(length):
        return "YES"
    else: 
        return "NO"