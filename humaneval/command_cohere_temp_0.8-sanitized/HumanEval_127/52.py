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
    Determine if the intersection of two closed intervals is prime
    """
    # Convert interval to rectangles to ease calculation
    r1_start, r1_end = max(s1), min(s1)
    r2_start, r2_end = max(s2), min(s2)

    # Calculate the overlap
    overlap_start = max(r1_start, r2_start)
    overlap_end = min(r1_end, r2_end)

    # Return no if no overlap
    if overlap_start > overlap_end:
        return "NO"

    overlap_length = overlap_end - overlap_start + 1

    if is_prime(overlap_length):
        return "YES"
    else:
        return "NO"