

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Pure math solution:
    # 
    # import math
    # return number - math.floor(number)
    # 
    # Or using string conversions:
    # 
    # return float(str(number).split('.')[1])
    # 
    # Or using modulo:
    # 
    # return number % 1
    
    # Using int() and -1:
    return number - int(number - 1)
