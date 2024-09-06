
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
    def get_sum_of_digits(num):
        sum_of_digits = 0
        for digit in str(num):
            sum_of_digits += int(digit)
        return sum_of_digits
    # sort the given list of integers
    sorted_list = sorted(nums, key=get_sum_of_digits)
    return sorted_list
