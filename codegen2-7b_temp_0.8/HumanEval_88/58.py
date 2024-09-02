
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
    if not array:
        return []
    nums = list(array)
    sorted_array = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i]+nums[j])%2 == 1:
                sorted_array.append(nums[i])
                nums[i] = nums[j]
                nums[j] = sorted_array[len(sorted_array)-1]
                sorted_array.pop()
                break
    return num
