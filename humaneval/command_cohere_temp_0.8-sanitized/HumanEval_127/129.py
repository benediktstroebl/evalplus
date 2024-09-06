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
    # Convert interval to integers
    s1, s2 = map(tuple, [s1, s2])
    # Calculate the intersection length (integer)
    x = max(s1[1], s2[1]) - min(s1[0], s2[0])
    # Check if there is a intersection
    if x <= 0:
        return "NO"
    # Check if the intersection length is prime
    if is_prime(x):
        return "YES"
    else: 
        return "NO"