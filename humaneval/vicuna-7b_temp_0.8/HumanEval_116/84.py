
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
    # Perform lexicographic order sorting
    arr = sorted(arr)

    # Create a dictionary with integers as keys and their binary representation
    # as values.
    binary_dict = {}
    for num in arr:
        binary_dict[num] = bin(num)[2:]

    # Convert the dictionary to an array
    binary_arr = [binary_dict[num] for num in arr]

    # Sort the array based on the number of ones in the binary representation
    binary_arr.sort()

    # Convert the array back to the list and return it
    return [int(num) for num in binary_arr]