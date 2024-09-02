
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
    def _sum_digits(num):
        """
        Helper function to calculate the sum of digits of a number.
        """
        return sum(int(d) for d in str(num))

    def _index(num):
        """
        Helper function to calculate the index of a number in the list.
        """
        return num - _sum_digits(num) - 1

    digits = sorted(nums, key=_sum_digits)
    nums = digits.copy()
    for i in range(len(nums)):
        if nums[i] == -1:
            nums[i] = digits.pop(0)
        elif nums[i] == 1:
            nums[i] = digits.pop()
    return nums