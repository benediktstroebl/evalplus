
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Handle the edge cases
    if a > b:
        return []
    if b - a < 2:
        return [a]
    
    # Get the range of integers between a and b
    min_val = a - 1
    max_val = b
    
    # Get the set of even digits
    even_digits = set(str(i).zfill(2) for i in range(min_val, max_val + 1))
    
    # Get the ascending order
    ascending_order = sorted(even_digits)
    
    # Return the set of even digits in ascending order
    return ascending_order
