
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
        number = abs(num)
        sum_of_digits = 0
        while number > 0:
            sum_of_digits += number % 10
            number //= 10
        if num < 0:
            sum_of_digits *= -1
        return sum_of_digits

    return sorted(nums, key=get_sum_of_digits)

