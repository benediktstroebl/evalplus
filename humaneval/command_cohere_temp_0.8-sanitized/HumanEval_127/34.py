def is_prime(n):
    """
    Checks if a number is prime
    Args:
        n (int): number to check
    Returns:
        bool: whether n is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Check the intersection of two closed intervals given as pairs (start, end).
    Args:
        s1,s2 (tuple): intervals
    
    Returns:
        str: "YES" if the intersection length is a prime number, otherwise "NO"
    """
    x = abs(max(s1[0], s2[0])) - abs(min(s1[0], s2[0]))
    y = abs(max(s1[1], s2[1])) - abs(min(s1[1], s2[1]))
    if x > y:
        x, y = y, x
    if x == 0:
        return "NO"
    if is_prime(x):
        return "YES"
    return "NO"