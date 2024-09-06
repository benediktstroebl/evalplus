
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
    # map digits to their powers
    nums = [[n, 10**i] for i, n in enumerate(nums)]
    nums = [n for n in nums if n[0]!= 0]  # remove zeros
    points = [sum(map(lambda x: x[0]*x[1], zip(map(int, str(abs(n[0]))), n[1:])))
              for n in nums]
    indices = range(len(nums))
    points = [p for p, i in sorted(zip(points, indices), key=itemgetter(0))]
    return [nums[i][0] for i in points]
