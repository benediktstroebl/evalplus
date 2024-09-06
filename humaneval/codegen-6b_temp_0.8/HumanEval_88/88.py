
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
    if len(array) <= 1:
        return array

    # as we need to reverse the array at the end, we will use a helper function
    def sort_array_helper(array, descending):
        if len(array) <= 1:
            return array

        # splitting the array into floors and ceilings
        start_of_floors = int(len(array) / 2)
        start_of_ceils = int(len(array) / 2)
        if (len(array) % 2) == 0:
            # even length
            start_of_ceils -= 1

        if descending:
            lo_sort, hi_sort = sort_array_helper(array[:start_of_floors], descending), sort_array_helper(array[start_of_ceils:], descending)
        else:
            lo_sort, hi_sort = sort_array_helper(array[:start_of_floors], ascending), sort_array_helper(array[start_of_ceils:], ascending)

        # sort the floors and ceilings, depending on the sign of the starting index
        if array[0] > array[-1]:
            lo_sort, hi_sort = hi_sort, lo_sort

        result = []

        # copying the sorted elements from lo_sort to result
        for i in range(len(lo_sort)):
            result.append(lo_sort[i])

        # copying the sorted elements from hi_sort to result
        for i in range(len(hi_sort)):
            result.append(hi_sort[i])

        return result

    return sort_array_helper(array, False)
