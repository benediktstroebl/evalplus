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
    # Convert the tuple (start, end) into a range object
    interval1 = range(s1[0], s1[1] + 1)
    interval2 = range(s2[0], s2[1] + 1)

    # Find the intersection of two intervals
    intersection = list(interval1 & interval2)

    # Check if the intersection is empty
    if len(intersection) == 0:
        return "NO"
    else:
        # Check if the length of the intersection is prime
        intersection_size = len(intersection)
        if is_prime(intersection_size):
            return "YES"
        else:
            return "NO"