
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
    def is_one(num):
        return sum(map(int, str(num))) == 1

    def index_order(l, index):
        return [i for i, num in enumerate(l) if i == index]

    def sort_by_points(nums):
        nums = [i for i in nums if is_one(i) is False]
        return sorted(nums, key=lambda i: (is_one(i), len(str(i)), i))

    return sort_by_points(nums)
