def is_prime(n):
    """
    Checks whether the given integer n is a prime number or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Determine whether the length of the intersection of two given closed intervals is a prime number or not.
    """
    # Convert the interval pair to a format that simplifies the computation of the intersection
    # i.e. (1, 3) -> [1, 3] and (2, 4) -> [2, 4]
    s1, s2 = [s1], [s2]
    s1 = [start for start, end in s1 if start <= end]
    s2 = [start for start, end in s2 if start <= end]

    # Check if the intervals don't intersect or their intersection length is 1, None or NaN
    if s1 == [] or s2 == [] or s1[0] == s2[0] or min(s1[0], s2[0]) > max(s1[1], s2[1]):
        return "NO"

    # Compute the intersection
    interval = [max(s1[0], s2[0]), min(s1[1], s2[1])]

    # Check if the intersection length is prime
    if is_prime(abs(interval[1] - interval[0])):
        return "YES"
    else:
        return "NO"