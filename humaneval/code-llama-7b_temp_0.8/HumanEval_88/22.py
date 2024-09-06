
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
    # O(nlogn) solution using quick sort
    def sort(arr, start, end):
        if end <= start + 1:
            return

        pivot = arr[start]
        left = start + 1
        right = end

        while right >= left:
            while right >= left and arr[left] < pivot:
                left += 1
            while right >= left and arr[right] > pivot:
                right -= 1
            if right >= left:
                arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        arr[start], arr[right] = arr[right], arr[start]
        sort(arr, start, right - 1)
        sort(arr, right + 1, end)

    if not array:
        return []

    start = 0
    end = len(array) - 1

    sum_of_first_and_last_values = array[0] + array[-1]

    if sum_of_first_and_last_values % 2 == 0:
        sort(array, start, end)
        return array

    sort(array, 0, len(array) - 1)
    return array[::-1]

