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
    Determine whether the length of the intersection of two closed intervals is a prime number or not.
    """
    # Convert interval pairs to tuples for easier comparison lateron
    s1, s2 = tuple(s1), tuple(s2)
    # Calculate the intersection if the intervals are overlapping
    if max(s1) < min(s2) or min(s1) > max(s2):
        return "NO"
    else:
        interval_length = max(s1) - min(s1)
        return "YES" if is_prime(interval_length) else "NO"