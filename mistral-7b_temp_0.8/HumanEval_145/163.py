
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
    # sort based on the sum of their digits
    # consider the same sum of the digits, order by index
    # input: list
    # output: list

    # sum of the digits
    # index
    # use a function for sorting
    # dict


    def sum_digits(num):
        return sum(map(int, str(num)))

    def index_digits(num):
        return num.index(num)

    # sorted(list, key=lambda i: sum_digits(i) + index_digits(i))
    return sorted(nums, key=lambda i: sum_digits(i), reverse=True)

    # list.sort(key=lambda i: sum_digits(i) + index_digits(i))
    # return nums

