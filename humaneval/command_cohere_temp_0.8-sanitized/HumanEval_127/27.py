def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Determine whether the length of intersection of two given closed intervals is a prime number.
    """
    # Convert interval to normalized form (min, max)
    s1 = (min(s1[0], s1[1]), max(s1[0], s1[1]))
    s2 = (min(s2[0], s2[1]), max(s2[0], s2[1]))

    # Determine intersection
    intersection = max(max(s1[0], s2[0]), min(s1[1], s2[1]))
    if min(s1[1], s2[1]) - max(s1[0], s2[0]) == 0:
        return "NO"
    length = (min(s1[1], s2[1]) - max(s1[0], s2[0]) + 1)

    if length == 1:
        return "NO"
    if is_prime(length):
        return "YES"
    else:
        return "NO"