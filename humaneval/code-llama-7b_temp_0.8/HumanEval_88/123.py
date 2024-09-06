
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
    # my solution
    def sort_by_sum(input_list):
        # input_list.sort(key=lambda x: x)
        input_list.sort()
        input_list.reverse()
        return input_list

    arr = array[:]
    if not arr:
        return []
    # check if first index value + last index value is odd or even, if odd then sort ascending, else sort descending.
    if (arr[0] + arr[-1]) % 2 == 0:
        return sort_by_sum(arr)
    else:
        return arr

    # lambdas
    # return array if len(array) <= 1 else sorted(array, key=lambda x: x if sum(array[0], array[-1]) % 2 == 0 else -x)

    # simpler
    # return array if len(array) <= 1 else sorted(array, key=lambda x: x if sum(array[0], array[-1]) % 2 == 0 else -x)

    # slice the list using index 0 and -1, if the sum is even then reverse, else no reverse.
    # return array if len(array) <= 1 else array[::-1] if sum(array[0], array[-1]) % 2 == 0 else array

    # while array:
    #     if sum(array[0], array[-1]) % 2 == 0:
    #         array.sort()
    #     else:
    #         array.sort(reverse=True)
    #     return array

    # return array if len(array) <= 1 else array[::-1] if sum(array[0], array[-1]) % 2 == 0 else array

    # return array if len(array) <= 1 else sorted(array, key=lambda x: x if sum(array[0], array[-1]) % 2 == 0 else -x)

    # return array if len(array) <= 1 else array[::-1] if sum(array[0], array[-1]) % 2 == 0 else array

    # return array if len(array) <= 1 else sorted
