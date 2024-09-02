
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

    # First step is to convert arr to binary and save as a dictionary
    # {arr: binary}
    for i in range(0, len(arr)):
        arr[i] = bin(arr[i]).replace("0b", "")

    # Order arr by the number of 1s in their binary representation
    sorted_arr = sorted(arr, key=lambda x: x.count('1'))

    # Order arr by their decimal value
    sorted_arr = sorted(sorted_arr, key=lambda x: int(x))

    # Return the sorted arr
    return sorted_arr

