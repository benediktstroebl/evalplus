
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
    # time complexity: O(n log n)
    # space complexity: O(n)
    # note: the following approach is brute force - can be made better
    if not nums:
        return nums

    nums_dict = {}
    for num in nums:
        total = sum(int(d) for d in str(num))
        if total not in nums_dict:
            nums_dict[total] = [num]
        else:
            nums_dict[total].append(num)

    result = []
    for key in sorted(nums_dict):
        for num in nums_dict[key]:
            result.append(num)
    return result

