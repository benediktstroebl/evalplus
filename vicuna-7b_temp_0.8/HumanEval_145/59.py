
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
    def _sum_digits(x):
        return sum(int(d) for d in str(x))

    digits = {str(x): _sum_digits(x) for x in nums}
    for i in range(1, len(nums)):
        num1 = nums[i]
        for j in range(i - 1, -1, -1):
            num2 = nums[j]
            diff = digits[str(num1)] - digits[str(num2)]
            if diff > 0:
                nums[i], nums[j] = nums[j], nums[i]
                digits[str(num1)] -= diff
                digits[str(num2)] += diff
    return nums

