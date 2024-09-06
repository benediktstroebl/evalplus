
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

    # nums = [1, 11, -1, -11, -12]
    # nums = []

    def digit_sum(num):
        # 11 + 1 = 12
        # 1 + 1 = 2
        # 11 + 1 + 1 = 13
        return sum(map(int, list(str(abs(num)))))
    def sort_key(num):
        return digit_sum(num), num

    return sorted(nums, key=sort_key)

