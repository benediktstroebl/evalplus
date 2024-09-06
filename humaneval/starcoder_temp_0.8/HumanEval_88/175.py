
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
    # quick sort, time complexity: O(nlogn), space complexity: O(logn)
    if not array:
        return []
    pivot = array[0]
    head = [x for x in array if x < pivot]
    tail = [x for x in array if x > pivot]
    if (sum(head) + sum(tail)) % 2 == 0:
        return head + [pivot] + tail
    else:
        return tail + [pivot] + head
