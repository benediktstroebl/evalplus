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
    # Convert interval to python intervals
    start1, end1 = s1
    start2, end2 = s2
    
    # Calculate the intersection size
    size_of_intersection = abs(end1 - start2) + abs(end2 - start1) - min(end1, end2) + max(start1, start2)

    if size_of_intersection <= 0:
        return "NO"
    elif is_prime(size_of_intersection):
        return "YES"
    else:
        return "NO"