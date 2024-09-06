def is_prime(n):
    """
    Checks if a number is prime
    Args:
        n (int): number to check if prime
    Returns:
        bool: true if n is prime, false otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Determine if the length of the intersection of two intervals is prime
    Args:
        s1 (tuple): first interval (start, end)
        s2 (tuple): second interval (start, end)
    Returns:
        str: "YES" if prime, "NO" if not prime or no intersection
    """
    if max(s1[0], s1[1]) > max(s2[0], s2[1]) or min(s1[0], s1[1]) < min(s2[0], s2[1]):
        return "NO"
    else:
        x = max(s1[1], s2[1]) - min(s1[0], s2[0])
        if is_prime(x):
            return "YES"
        else:
            return "NO"