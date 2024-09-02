
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
    nums_with_points = []

    for num in nums:
        points = 0

        for digit in str(abs(num)):
            points += int(digit)

        nums_with_points.append((num, points, abs(nums.index(num))))

    sorted_nums_with_points = sorted(nums_with_points, key=lambda x: (x[1], x[2]))

    return [num[0] for num in sorted_nums_with_points]
