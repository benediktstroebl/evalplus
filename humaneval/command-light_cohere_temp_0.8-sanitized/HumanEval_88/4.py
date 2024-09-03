def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum of the first and last index values is odd,
    or sort it in descending order if the sum of the first and last index values is even.

    Note: 
    * The array must not be modified.
    """
    array[:0] = array  # Shifting to the left side
    array = [x for x in array if x >= array[0]] + array[:0]  # Filtering elements
    array = array + array[::-1]  # Reversing the array
    return array[:]  # Returning a copy