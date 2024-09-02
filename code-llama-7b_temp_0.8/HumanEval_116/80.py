
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
    my_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for num in arr:
        # my_dict[bin(num).count("1")] += [num]
        # my_dict[len(bin(num).replace("0b", "").rstrip("0"))] += [num]
        my_dict[int(bin(num).count("1"))].append(num)
        my_dict[int(len(bin(num).replace("0b", "").rstrip("0")))].append(num)

    # Flattened dictionary values
    return [val for sublist in list(my_dict.values()) for val in sublist]

