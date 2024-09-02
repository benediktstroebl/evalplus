

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # check if a and b are positive
    if a < 0 or b < 0:
        raise ValueError("One or both arguments must be non-negative")
    
    # if a and b are equal, they have no greatest common divisor
    if a == b:
        return 1
    
    # find all common factors of a and b
    factors = [2, 3, 4, 6, 8, 9, 10]
    while len(factors) > 1:
        # find highest common factor
        highest_common_factor = 1
        for factor in factors:
            if factor > a and factor > b:
                highest_common_factor = factor
                break
        else:
            # if no highest common factor is found, set it to 1
            highest_common_factor = 1
        factors = [highest_common_factor]
        
        # try to find a common divisor
        for remainder in divmod(a, highest_common_factor):
            for remainder in divmod(b, highest_common_factor):
                if remainder == 0:
                    return highest_common_factor
                
    # if no common divisor is found, return 1
    return 1