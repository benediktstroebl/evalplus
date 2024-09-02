
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    # DO NOT use the built-in `sorted()` function.
    # Instead, use the `for` loop to iterate over each element in the list,
    # and `insert` the current element to the correct index, based on the sum of digits.
    # The time complexity of this function is O(n log n) because of the built-in `sorted` function.
    # The space complexity of this function is O(1).

    for i in range(1, len(nums)):
        for j in range(i - 1, -1, -1):
            if sum(int(x) for x in str(nums[i])) > sum(int(x) for x in str(nums[j])) or (sum(int(x) for x in str(nums[i])) == sum(int(x) for x in str(nums[j])) and i < j):
                nums.insert(j + 1, nums.pop(j))
                break
    return nums
