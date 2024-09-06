def is_prime(n):
    """
    Checks whether the given integer n is a prime number or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Determine whether the length of intersection of two given closed intervals is a prime number or not.
    """
    # Convert the interval pair to a tuple.
    interval = tuple(sorted([s1, s2]))
    # Calculate the length of the intersection.
    length = abs(interval[0][1] - interval[1][0])
    if not length:  # No intersection.
        return "NO"
    elif is_prime(length):
        return "YES"
    else:
        return "NO"