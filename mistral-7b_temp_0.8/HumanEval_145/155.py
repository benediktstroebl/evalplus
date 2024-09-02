
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

    def sum_of_digits(x):
        sum = 0
        x = str(x)
        for i in x:
            sum += int(i)
        return sum

    def compare(a, b):
        if sum_of_digits(a) == sum_of_digits(b):
            if a < b:
                return -1
            else:
                return 1
        elif sum_of_digits(a) < sum_of_digits(b):
            return -1
        else:
            return 1

    return sorted(nums, key=sum_of_digits, cmp=compare)

