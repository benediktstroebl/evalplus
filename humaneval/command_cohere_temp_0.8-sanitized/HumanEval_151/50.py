def double_the_difference(lst):
    """
    Sum of squares of odd integers from the list, while ignoring negative or non-integer numbers.

    :param lst: List of numbers.
    :return: Sum of squares of odd integers or 0 if the list is empty.
    """
    result = 0
    for num in lst:
        if num % 2 == 1 and num >= 0 and isinstance(num, int):
            result += num ** 2

    return result