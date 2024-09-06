
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    # Zip the array into a list of tuples
    # The first value will be the index of the array
    # The second value will be the value of the array
    # eg: [(0, 2), (1, 4), (2, 3), (3, 0), (4, 1), (5, 5)]
    zipped = list(enumerate(array))

    # Using the zip() builtin to transpose the values
    # eg: [[0, 1, 2, 3, 4, 5], [2, 4, 3, 0, 1, 5]]
    transposed = zip(*zipped)

    # Sort the first value of the transposed list
    # eg: [0, 1, 2, 3, 4, 5]
    first_values = sorted(transposed[0])

    # Zip back up the list
    # eg: [(0, 2), (1, 4), (2, 3), (3, 0), (4, 1), (5, 5)]
    zipped = zip(first_values, transposed[1])

    # Return a list of tuples as a list of integers
    # eg: [2, 4, 3, 0, 1, 5]
    return [value for _, value in zipped]

