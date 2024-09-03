def largest_smallest_integers(numbers_list):
    """Returns a tuple with the largest negative integer and the smallest positive integer.

    Args:
        numbers_list (list): A list of integers with both positive and negative values.

    Returns:
        tuple: A tuple containing the largest negative integer and the smallest positive integer.
                Both values are returned as None if the respective integers are not found.

    Examples:
        >>> largest_smallest_integers([2, 4, 1, 3, 5, 7])
        (None, 1)

        >>> largest_smallest_integers([])
        (None, None)

        >>> largest_smallest_integers([0])
        (None, None)
    """
    largest_neg = None
    smallest_pos = None

    for num in numbers_list:
        if num < 0:
            if largest_neg is None or num > largest_neg:
                largest_neg = num
        elif num > 0:
            if smallest_pos is None or num < smallest_pos:
                smallest_pos = num

    return largest_neg, smallest_pos