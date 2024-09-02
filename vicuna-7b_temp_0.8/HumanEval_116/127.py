
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
    # Helper function to convert an integer to its binary representation
    def to_binary(x):
        return str(x).zfill(bin_length)

    def compare(a, b):
        # Compare binary representations of the numbers
        return cmp(to_binary(a), to_binary(b))

    # Sort the array by converting each element to its binary representation
    return sorted(arr, key=lambda x: to_binary(x), cmp=compare)