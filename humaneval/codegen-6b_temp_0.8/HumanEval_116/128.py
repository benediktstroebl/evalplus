
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
    # Convert the array to a dictionary
    # Loop through the dictionary, adding a list of one with value = key and
    # count = 1
    # Add another list with value = key and count = 1
    # Loop through the dictionary again, adding a list of count by multiplying by 2
    # The result of the function is a sorted list of tuples
    arr_len = len(arr)
    char_dict = {}
    for i in range(arr_len):
        if arr[i] not in char_dict:
            char_dict[arr[i]] = [arr[i], 1]
            continue
        char_dict[arr[i]].append(arr[i])
    result = []
    for key, value in char_dict.items():
        result.append([key, value])
    result.sort(key=itemgetter(0))
    return [x[0] for x in result]
