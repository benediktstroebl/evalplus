def exchange(list1, list2):
    """
    Implements the function from the problem statement.
    Args:
        list1 (list of numbers),
        list2 (list of numbers)
    Returns:
    bool
    """
    if len(list1) != len(list2):
        return False
    for num1, num2 in zip(list1, list2):
        if num1 % 2 != num2 % 2:
            return False
    return True