def is_prime(n):
    """
    Checks whether a positive integer 'n' is a prime number or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Checks whether the length of the intersection of two given intervals is a prime number or not.
    """
    # Convert intervals to tuples for easier comparison
    s1, s2 = tuple(s1), tuple(s2)
    # Calculate the length of the intersection of two intervals
    length = max(max(s1), max(s2)) - min(min(s1), min(s2))

    if length < 1:
        return "NO"
    elif is_prime(length):
        return "YES"
    else: 
        return "NO"