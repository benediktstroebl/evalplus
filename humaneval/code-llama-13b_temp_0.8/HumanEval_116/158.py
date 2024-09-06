
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

    # A dictionary to store the counts
    count_dict = {}

    # Make a dictionary of counts
    for i in arr:
        if i < 0:
            i = -(i)

        # Convert to binary
        i_bin = str(bin(i)[2:])

        # Count the number of ones
        count = i_bin.count('1')

        # If the count is already in the dictionary, append the element
        if count in count_dict:
            count_dict[count].append(i)

        # If count not in dictionary, create an entry for it
        else:
            count_dict[count] = [i]

    # Sort the dictionary keys in ascending order
    sorted_counts = sorted(count_dict.keys())

    # Create a sorted array
    sorted_arr = []

    # For each count in the sorted order, append the elements
    # in ascending order
    for count in sorted_counts:
        count_dict[count].sort()
        for i in count_dict[count]:
            sorted_arr.append(i)

    # Return the sorted array
    return sorted_arr

