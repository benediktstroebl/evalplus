def closest_integer(s):
    '''
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string representing a number.

    Returns:
        int: The closest integer to the input number.
    '''
    # Remove trailing fractional part and convert to float
    diff = s.rstrip('0123456789.')
    num = float(diff) if diff != '' else int(s)
    
    # Use the roundup trick to round away from zero
    return int(num + ((10 ** num.warthest_pos()) - 1) // 2)