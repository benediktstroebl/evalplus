
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    # Check if array is empty
    if not arr:
        return []

    # Initialize result list
    result = []

    # Sort each number
    for num in arr:
        # If number has only one digit (1), add it to result list
        if len(str(num)) == 1:
            result.append(num)
        else:
            # If number has more than one digit, add it to result list after sorting
            result.append(num)
            # Sort the number
            result.sort(key=lambda x: sum(int(d) for d in x))

    return result
