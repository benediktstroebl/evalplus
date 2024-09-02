
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
    n = len(nums)
    if n == 0:
        return []

    digit_sums = [sum(int(digit) for digit in str(num)) for num in nums]
    result = sorted(digit_sums, key=digit_sums.index)

    for i in range(n - 1, -1, -1):
        j = i + 1
        while j < n and result[j] == result[i]:
            result[i], result[j] = result[j], result[i]
            j += 1

    return result