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
    Checks whether the length of the intersection of two closed intervals is a prime number or not.
    """
    # Convert Interval to Python's style
    s1 = [s1[0], s1[1]]
    s2 = [s2[0], s2[1]]

    # Calculate the intersection interval
    x = max(s1[0], s2[0]);
    y = min(s1[1], s2[1])
    if x > y:
        return "NO"

    # Check prime
    if is_prime(y-x+1):
        return "YES"
    else:
        return "NO"