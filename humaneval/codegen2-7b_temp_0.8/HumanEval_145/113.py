
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
    def compare(x, y):
        x_sum = sum(list(map(int, str(x))))
        y_sum = sum(list(map(int, str(y))))
        return x_sum - y_sum if x_sum!= y_sum else x - y
    return sorted(nums, key=cmp_to_key(compare
