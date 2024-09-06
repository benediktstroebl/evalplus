def is_prime(n):
    """
    Checks whether a number is prime
    Args:
        n (int): number to check
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
        s1 (tuple): first interval
        s2 (tuple): second interval
    """
    if not (s1[0] <= s2[1] and s1[1] >= s2[0]):
        return "NO"
    length_of_intersection = max(s1[1], s2[1]) - min(s1[0], s2[0]) + 1
    if is_prime(length_of_intersection):
        return "YES"
    else: 
        return "NO"