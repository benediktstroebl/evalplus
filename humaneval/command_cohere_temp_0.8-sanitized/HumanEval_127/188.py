def is_prime(n):
    """
    Checks whether a number is prime

    Args:
        n (int): Number to check
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Checks whether the intersection of two intervals is a prime number

    Args:
        s1 (tuple): First interval (start, end)
        s2 (tuple): Second interval (start, end)

    Returns:
        str: "YES" if the intersection is prime, "NO" otherwise
    """
    x = max(max(s1), max(s2)) - min(min(s1), min(s2))
    if x <= 0:
        return "NO"
    if is_prime(x):
        return "YES"
    else:
        return "NO"