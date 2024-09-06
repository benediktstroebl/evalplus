
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
    def sum_digits(num):
        return sum(int(d) for d in str(num))

    n = len(nums)
    if n == 0:
        return []
    else:
        result = [nums[i] for i in range(n)]
        for i in range(1, n):
            j = i
            while sum_digits(result[j]) < sum_digits(result[i-1]):
                result[j], result[i-1] = result[i-1], result[j]
                j -= 1
        return result
