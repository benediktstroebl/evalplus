
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

    def get_points(num):
        if num < 0:
            num = -num
        return sum(map(int, str(num)))

    def get_order(a, b):
        a_points = get_points(a)
        b_points = get_points(b)
        if a_points == b_points:
            return a - b
        return a_points - b_points

    return sorted(nums, key=cmp_to_key(get_order))

