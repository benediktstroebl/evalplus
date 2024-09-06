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
    # Convert the interval pair to a tuple for easier comparison.
    interval = (max(s1[0], s2[0]), min(s1[1], s2[1]))
    if max(s1[1], s2[1]) <= min(s1[0], s2[0]):
        return "NO"
    else:
        length_of_intersection = abs(interval[1] - interval[0])
        if is_prime(length_of_intersection):
            return "YES"
        else:
            return "NO"