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
    # Convert interval to python intervals
    start1, end1 = s1
    start2, end2 = s2
    
    # Calculate the intersection
    intersect_start = max(start1, start2)
    intersect_end = min(end1, end2)
    
    # Check if there is an intersection
    if intersect_start > intersect_end:
        return "NO"
    
    intersect_length = intersect_end - intersect_start + 1
    
    if is_prime(intersect_length):
        return "YES"
    else:
        return "NO"