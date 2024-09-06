
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
    # 1. 0 <= num < 1000
    # 2. [0, 50000]
    nums = []
    pos = 0
    neg = 0
    while pos < len(array) and neg < len(array):
        if array[pos] < 0:
            nums.insert(0, array[neg])
            neg += 1
        elif array[neg] > 0:
            nums.insert(0, array[pos])
            pos += 1
        else:
            if sum(array[:2]) % 2 == 0:
                nums.insert(0, array[pos])
                pos += 1
            else:
                nums.insert(0, array[neg])
                neg += 1

    if pos < len(array):
        nums.insert(0, array[pos])
    if neg < len(array):
        nums.insert(0, array[neg])

    return nums
