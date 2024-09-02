
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
    list = []
    def sort(n):
        if n == 0:
            return 0
        else:
            sum = 0
            while n != 0:
                sum += n % 10
                n /= 10
            return sum
    for i in nums:
        if i >= 0:
            list.append(sort(i))
        else:
            list.append(sort(i) * -1)
    list.sort()
    return list

