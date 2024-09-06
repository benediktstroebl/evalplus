
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
    def get_sum_of_digits(n):
        sum = 0
        while n > 0:
            sum += n % 10
            n //= 10
        return sum

    order_nums = []
    for i in range(len(nums)):
        order_nums.append([nums[i], get_sum_of_digits(nums[i]), i])
    order_nums.sort()
    return [order[0] for order in order_nums]
