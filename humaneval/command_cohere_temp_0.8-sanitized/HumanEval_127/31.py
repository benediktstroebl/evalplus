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
    # Convert interval to integers
    s1, s2 = map(tuple, [(start, end) for start, end in [(s1[0], s1[1]), (s2[0], s2[1])]])

    # Calculate the intersection length
    interval_length = abs(max(s1[1], s2[1]) - min(s1[0], s2[0]))

    # Check if the intersection length is prime
    if is_prime(interval_length):
        return "YES"
    else:
        return "NO"