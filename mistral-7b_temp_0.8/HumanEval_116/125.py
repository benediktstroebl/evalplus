
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
    # If there are no integers in the array, return an empty list
    if not arr:
        return []

    # Initialize a dictionary to store the counts of ones in each integer
    counts = {}

    # Iterate over each integer in the array
    for num in arr:

        # Convert the integer to binary
        bin_num = bin(num)[2:]

        # Count the number of ones in the binary representation
        num_ones = bin_num.count('1')

        # If the integer is already in the dictionary, increment its count by 1
        if num in counts:
            counts[num] += 1
        # If the integer is not in the dictionary, initialize its count to 1
        else:
            counts[num] = 1

    # Sort the dictionary by its keys in ascending order
    sorted_dict = {key: value for key, value in sorted(counts.items(), key=lambda x: (x[1], x[0]))}

    # Convert the sorted dictionary back to a list of integers
    sorted_list = [int(
