
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
    # 1. Create a dict with numbers as key and number of 1's as value
    # 2. Sort the dict based on keys
    # 3. Add the dict values in list
    if not arr:
        return []
    # Create a dictionary with key as number and value as number of ones
    ones_dict = {}
    for x in arr:
        if x in ones_dict:
            ones_dict[x] += 1
        else:
            ones_dict[x] = count_ones(x)
    sorted_dict = sorted(ones_dict.items(), key=lambda x: x[0])
    return [x[0] for x in sorted_dict]

