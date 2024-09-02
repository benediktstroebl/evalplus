
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    start, stop = a, b
    if (start % 2!= 0) or (stop % 2!= 0):
        stop -= 1
    return [x for x in range(start, stop+1, 2) if x <= stop and x >= start]
    
    
