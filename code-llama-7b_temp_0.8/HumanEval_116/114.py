
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
    # Convert each integer to binary string representation.
    bin_strs = [bin(num)[2:] for num in arr]
    # Zip together the strings and the original integers.
    zipped = zip(bin_strs, arr)
    # Count the number of ones in each binary string.
    sorted_zipped = sorted(zipped, key=lambda x: (x[0].count("1"), x[0].count("0"), x[1]))
    # Convert back to integers and return.
    return [num for (_, num) in sorted_zipped]
