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
    # Convert interval to tuple (start, end)
    x = (max(s1[0], s2[0]), min(s1[1], s2[1]))
    # Check if the two intervals intersect
    if x[0] >= x[1]:
        return "NO"
    else:
        # Calculate the length of the intersection and check if it's prime
        length = x[1] - x[0] + 1
        if is_prime(length):
            return "YES"
        else:
            return "NO"