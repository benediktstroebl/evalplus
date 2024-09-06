
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
    # your code here
    # function to sort
    def sort_nums(nums):
        nums.sort(key=lambda x: x[0])
        for i in range(len(nums)):
            nums[i] = nums[i][1]

    # making a list of tuples
    list_nums = []
    for i in range(len(nums)):
        digits_sum = 0
        for j in range(len(str(nums[i]))):
            digits_sum += int(str(nums[i])[j])
        list_nums.append((digits_sum, nums[i]))

    # sorting the list
    sort_nums(list_nums)

    # returning the sorted list
    return list_nums

