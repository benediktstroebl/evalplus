
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
    # build a dict of sum-of-digits-to-list-of-numbers-with-that-sum
    sums_to_nums = {}
    for num in nums:
        sum = sum_of_digits(num)
        if sum not in sums_to_nums:
            sums_to_nums[sum] = []
        sums_to_nums[sum].append(num)
    # build the output list
    output = []
    for num in nums:
        sum = sum_of_digits(num)
        nums_with_sum = sums_to_nums[sum]
        # if num is the max, put it first
        if num == max(nums_with_sum):
            output.insert(0, num)
        # otherwise put it last
        else:
            output.append(num)
    return output

