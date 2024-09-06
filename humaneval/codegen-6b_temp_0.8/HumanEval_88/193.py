
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
    # base case, only one element in the array
    if len(array) == 1:
        return array

    # split the array into two array
    less_than_pivot = []
    greater_than_pivot = []

    # split the array into two array using the pivot
    pivot = array[0]
    for item in array[1:]:
        if item < pivot:
            less_than_pivot.append(item)
        else:
            greater_than_pivot.append(item)

    # call the sort_array function to sort the array
    less_than_pivot = sort_array(less_than_pivot)
    greater_than_pivot = sort_array(greater_than_pivot)

    # merge the two array
    return merge_array(less_than_pivot, greater_than_pivot)

