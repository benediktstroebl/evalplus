def is_prime(n):
    """
    Checks if a number is prime
    Args:
        n (int): number to check if prime
    Returns:
        bool: true if prime, false otherwise
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Check if the intersection of two intervals is a prime number
    Args:
        s1 (tuple): first interval tuple (start, end)
        s2 (tuple): second interval tuple (start, end)
    Returns:
        str: "YES" if prime, otherwise "NO"
    """
    if not ((s1[0] >= s2[0]) and (s1[1] <= s2[1])) and not ((s2[0] >= s1[0]) and (s2[1] <= s1[1])):
        return "NO"
    else:
        interval_length = max(s1[1], s2[1]) - min(s1[0], s2[0])
        if is_prime(interval_length):
            return "YES"
        else:
            return "NO"