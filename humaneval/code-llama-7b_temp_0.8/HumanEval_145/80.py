
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
    new_list = []
    for i in nums:
        total = 0
        a = str(i)
        for j in a:
            total += int(j)
        new_list.append((total, i, a))
    return [b for (total, a, c) in sorted(new_list) for b in (a, c)]






































