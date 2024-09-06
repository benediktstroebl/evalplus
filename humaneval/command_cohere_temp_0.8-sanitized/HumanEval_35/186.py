def max_element(l: list):
    """Return maximum element in the list.

    :param l: A list of numbers.
    :type l: list
    :return: The maximum element in the list.
    :rtype: int or float
    """
    if not l:
        raise ValueError("Input list is empty")
    return max(l)