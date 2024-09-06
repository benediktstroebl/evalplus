def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Determine whether the length of intersection of two given closed intervals is a prime number.
    """
    # Convert the interval pair to a tuple of (start, end)
    interval = (max(s1[0], s2[0]), min(s1[1], s2[1]))
    length = interval[1] - interval[0]

    if length < 0:
        return "NO"
    if is_prime(length):
        return "YES"
    else:
        return "NO"