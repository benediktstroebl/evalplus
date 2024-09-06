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
    Determine if the length of the intersection of two closed intervals is prime
    """
    # Convert the interval pairs to dictionaries with start and end values
    interval1 = {'start': s1[0], 'end': s1[1]}
    interval2 = {'start': s2[0], 'end': s2[1]}

    # Determine if the intervals intersect at all
    if interval1['end'] < interval2['start'] or interval2['end'] < interval1['start']:
        return "NO"

    # Calculate the intersection interval from the two input intervals
    x = max(interval1['end'], interval2['end'])
    y = min(interval1['start'], interval2['start'])
    intersection_length = x - y + 1

    # Check if the intersection length is prime
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"