def is_prime(n):
    """
    Checks whether a number is prime

    Args:
        n (int): Number to check
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    """
    Checks whether the intersection of two intervals is a prime number

    Args:
        s1 (tuple): First interval (start, end)
        s2 (tuple): Second interval (start, end)

    Returns:
        str: "YES" if the intersection is prime, otherwise "NO"
    """
    if not s1 or not s2:
        return "NO"
    intex_start = max(s1[0], s2[0])
    intex_end = min(s1[1], s2[1])
    if intex_start > intex_end:
        return "NO"
    intex_len = intex_end - intex_start
    if is_prime(intex_len):
        return "YES"
    return "NO"