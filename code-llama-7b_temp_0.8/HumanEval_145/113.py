
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
    # Use a dict to maintain the points for each number
    points = {}
    for num in nums:
        total_points = 0
        for digit in str(num):
            total_points += int(digit)
        points[num] = total_points

    ordered_points = sorted(points.items(), key=lambda x: x[1])
    result = []
    for pair in ordered_points:
        result.append(pair[0])

    return result

