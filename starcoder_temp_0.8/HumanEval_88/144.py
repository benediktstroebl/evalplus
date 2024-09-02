
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

    def helper(array, start, end):
        if end - start == 0 or end - start == 1:
            return
        mid = start + ((end - start) // 2)
        helper(array, start, mid)
        helper(array, mid, end)
        helper_merge(array, start, mid, end)

    def helper_merge(array, start, mid, end):
        merged = []
        start2 = mid
        while start < mid and start2 < end:
            if array[start] <= array[start2]:
                merged.append(array[start])
                start += 1
            else:
                merged.append(array[start2])
                start2 += 1

        while start < mid:
            merged.append(array[start])
            start += 1

        while start2 < end:
            merged.append(array[start2])
            start2 += 1

        for i in range(start, end):
            array[i] = merged[i - start]

    helper(array, 0, len(array))
    return array

