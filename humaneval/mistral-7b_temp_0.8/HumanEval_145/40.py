
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
        while i > 0:
            b.append(i%10)
            i //= 10
        b.reverse()
        a.append(sum(b))
    a.sort()
    return [nums[i] for i in range(len(a)) if a[i]==a[0]] + [nums[i] for i in range(len(a)) if a[i]==a[1]]
