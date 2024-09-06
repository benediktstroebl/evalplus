def truncate_number(number):
    """
    Returns the decimal part of the number (float) for positive floating-point input,
    returns 0 if passed an integer, and -0.1 if negative decimal passed.
    
    Parameters:
    number (float or int): Number to be truncated 
    
    Returns:
    float
    """
    if isinstance(number, int): 
        return 0.0
    elif number < 0:
        return -0.1
    else:
        return number - int(number)