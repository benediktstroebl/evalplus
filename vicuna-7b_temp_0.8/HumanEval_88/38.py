
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
    def sum_of_range(arr):
        """
        Sum of range
        """
        sum = 0
        for i in range(1, len(arr)):
            sum += arr[i]
        return sum

    def partition(arr):
        """
        partition
        """
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if sum_of_range(arr[mid-1:mid+1]) % 2 != 0:
                low = mid + 1
            else:
                high = mid
        return arr[low:high + 1]

    arr = sorted(array)
    return partition(arr)[::-1]