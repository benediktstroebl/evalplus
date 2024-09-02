
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
    def _sort_by_index(lst):
        def get_sum_of_digits(num):
            sum_of_digits = 0
            while num != 0:
                sum_of_digits += num % 10
                num //= 10
            return sum_of_digits

        lst_copy = lst[:]
        lst_copy.sort(key=lambda x: get_sum_of_digits(x))
        return lst_copy

    return _sort_by_index(nums)

