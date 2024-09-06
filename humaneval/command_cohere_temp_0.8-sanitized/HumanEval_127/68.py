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
    Determine whether the length of the intersection of two closed intervals is a prime number.
    """
    # Convert the interval pairs to tuples
    start1, end1 = s1
    start2, end2 = s2

    # Calculate the intersection length
    interval_length = abs(end1 - start1) * abs(end2 - start2)

    # Determine the length of the intersection and return appropriate answer
    if interval_length == 0:
        return "NO"
    elif is_prime(interval_length):
        return "YES"
    else: 
        return "NO"