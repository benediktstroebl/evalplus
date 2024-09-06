def is_prime(n):
    """
    Checks whether a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Determine whether the length of the intersection of two closed intervals is prime
    """
    # Convert the interval pairs to integers (inclusive)
    s1, s2 = map(int, (s1, s2))

    # Calculate the intersection length (inclusive)
    length = max(s1, s2) - min(s1, s2) + 1

    if length == 0:
        return "NO"
    if is_prime(length):
        return "YES"
    else:
        return "NO"