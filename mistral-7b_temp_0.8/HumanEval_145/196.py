
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
    def num_to_sum(n):
        s = 0
        while n > 0:
            s += n % 10
            n /= 10
        return s

    def compare(i1, i2):
        return num_to_sum(i1) - num_to_sum(i2)
    return sorted(nums, key=compare)
