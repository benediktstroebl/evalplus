
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
    # TODO: Write your solution here
    lst = []
    for num in nums:
        sum = 0
        for x in str(num):
            sum += int(x)
        lst.append([sum, num])
    lst = sorted(lst)
    lst = [i[1] for i in lst]
    return lst

