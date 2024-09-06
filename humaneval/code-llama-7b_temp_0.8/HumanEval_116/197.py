
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
    # if no elements present
    if len(arr) == 0:
        return []

    # if only one element present
    elif len(arr) == 1:
        return arr

    # else separate the array in 3 lists based on number of ones in the binary representation
    else:
        # store the number of ones in the binary representation of the given number in an integer
        num_ones = (bin(x).count("1") for x in arr)
        # create empty lists
        arr_ones = []
        arr_no_ones = []
        arr_mult_ones = []
        # populate the list based on number of ones
        for i in range(len(arr)):
            if num_ones[i] == 1:
                arr_ones.append(arr[i])
            elif num_ones[i] > 1:
                arr_mult_ones.append(arr[i])
            else:
                arr_no_ones.append(arr[i])
        # sort the lists
        arr_no_ones.sort()
        arr_ones.sort()
        arr_mult_ones.sort()
        # create a new array
        new_arr = []
        # populate the new array
        for i in range(len(arr)):
            if arr_no_ones:
                new_arr.append(arr_no_ones.pop(0))
            elif arr_ones:
                new_arr.append(arr_ones.pop(0))
            elif arr_mult_ones:
                new_arr.append(arr_mult_ones.pop(0))
        return new_arr

