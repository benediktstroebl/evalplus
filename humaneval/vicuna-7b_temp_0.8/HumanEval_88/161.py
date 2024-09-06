
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
    n = len(array)
    # create a new array and fill it with the original array values
    sorted_array = [array[i] for i in range(n)]
    # sort the array using heapq.heappush()
    for i in range(n-1, 0, -1):
        # if the sum of the first and last elements of the sub-array is odd, sort the sub-array in ascending order
        if sum(sorted_array[i:i+2)) % 2 == 1:
            heapq.heappush(sorted_array, sorted_array[i])
        # if the sum of the first and last elements of the sub-array is even, sort the sub-array in descending order
        else:
            heapq.heappush(sorted_array, sorted_array[i-1])
    return sorted_array