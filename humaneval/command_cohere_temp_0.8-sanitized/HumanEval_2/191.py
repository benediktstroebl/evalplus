def truncate_number(number):
    """ Returns the decimal part of the number
    Args:
        number (float): positive floating point number
    Returns:
        float: decimal part of the number
    """
    return number - int(number)