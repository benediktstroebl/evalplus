def special_factorial(n):
    """
    Brazilian factorial is defined as:
        brazilian_factorial(n) = n!. * (n-1)! * ... * 1
    where n > 0

    Returns:
        int: Special factorial number
    """
    return n*(n*special_factorial(n-1))