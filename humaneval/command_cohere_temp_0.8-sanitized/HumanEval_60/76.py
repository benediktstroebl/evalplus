def sum_to_n(n):
    """Returns the sum of the first n integers.
    Note: this function should only be used for numericals greater than 0.
    Args:
        n (int): The last number to be included in the sum
    Returns:
        int: The sum of the first n integers
    """
    # The following code uses the arithmetic series sum formula to calculate the sum of the first n integers.
    # The formula is sum = (n*(n+1))/2.
    return int(n*(n+1)/2)