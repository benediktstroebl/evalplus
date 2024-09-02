
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
    # Convert the input array to a list of integers
    int_arr = list(map(int, arr))

    # Create a dictionary to map each number to its count of ones
    ones_dict = {}
    for i in int_arr:
        count = 0
        while i > 0:
            if i % 2 == 0:
                count += 1
            i = i // 2
        ones_dict[i] = count

    # Sort the dictionary by count of ones in descending order
    sorted_ones_dict = sorted(ones_dict, key=lambda x: x[1], reverse=True)

    # Sort the input array based on the sorted dictionary values
    sorted_arr = sorted(int_arr, key=lambda x: sorted_ones_dict[x])

    return sorted_arr