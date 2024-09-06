
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

    # your code goes here
    def digit_sum(num):
        return sum([int(d) for d in str(num)])

    new_list = []
    for i in range(len(nums)):
        new_list.append((digit_sum(nums[i]), nums[i]))

    new_list.sort()

    return [num for _, num in new_list]


