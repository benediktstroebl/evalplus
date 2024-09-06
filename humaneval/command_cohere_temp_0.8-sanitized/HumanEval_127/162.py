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
    # Convert interval to sorted format {start, end}
    s1 = sorted([s1[0], s1[1]])
    s2 = sorted([s2[0], s2[1]])

    # Check if there is an intersection
    if s1[0] > s2[1] or s2[0] > s1[1]:
        return "NO"

    # Calculate the intersection and check if it is prime
    x = max(s1[1], s2[1]) - min(s1[0], s2[0])
    if is_prime(x):
        return "YES"
    else:
        return "NO"