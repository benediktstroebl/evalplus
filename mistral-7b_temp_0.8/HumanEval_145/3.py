
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
    a = []
    for i in nums:
        b = []
        sum = 0
        for j in str(i):
            sum += int(j)
        b.append(sum)
        b.append(i)
        a.append(b)
    a = sorted(a, key=lambda x: (x[0], x[1]))
    for i in a:
        print(i)
