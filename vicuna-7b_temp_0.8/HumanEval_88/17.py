
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
    # This is an example of the slowest possible algorithm.
    # You should use a more efficient sorting algorithm like quicksort or mergesort.
    n = len(array)
    if n <= 1:
        return array
    # If the array is not empty and its size is greater than 1,
    # We can use the algorithm to sort the array.
    middle = n // 2
    smaller_half = [x for x in array if x >= middle]
    bigger_half = [x for x in array if x <= middle]
    smaller_half.sort(reverse=True)
    bigger_half.sort(reverse=True)
    array.extend(smaller_half)
    array.extend(bigger_half)
    return array
