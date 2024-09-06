def max_element(l: list):
    """Return maximum element in the list.

    :param l: A list of numbers.
    :type l: list
    :return: The maximum element in the list.
    :rtype: int
    """
    # Initialize maxval to the first element in the list
    maxval = l[0]
    # Iterate over the list, and update maxval to the largest of maxval and the current element.
    for x in l:
        if x > maxval:
            maxval = x
    # Return the final maxval
    return maxval