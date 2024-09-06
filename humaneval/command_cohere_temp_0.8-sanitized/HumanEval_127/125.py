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
    # Convert the interval pairs to integers.
    s1, s2 = map(sum, zip(s1, s2))
    # Calculate the intersection length as an integer.
    length = abs(s2 - s1)
    # Check if the intersection length is prime.
    if is_prime(length):
        return "YES"
    else:
        return "NO"