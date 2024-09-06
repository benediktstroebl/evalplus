
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
    # no digits, return original array
    if not nums:
        return nums

    # sum of digits
    def sum_of_digits(num):
        if num < 0:
            num = num * -1
        digits = []
        while num > 0:
            digits.append(num % 10)
            num = num // 10
        return sum(digits)

    # returns the index of the first matching item
    # if not found, return -1
    def index_of(item, indexes):
        if not indexes:
            return -1
        for i in indexes:
            if item == indexes[i]:
                return i
        return -1

    sorted_by_digits = sorted(nums, key = sum_of_digits)

    new_indexes = [i for i, num in enumerate(nums) if num != sorted_by_digits[i]]

    new_nums = []
    for num in sorted_by_digits:
        index
