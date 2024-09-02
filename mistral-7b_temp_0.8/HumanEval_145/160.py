
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
    def number_of_digits(num):
        count = 0
        while num != 0:
            num = num // 10
            count += 1
        return count

    def sum_of_digits(num):
        sum = 0
        while num != 0:
            num, mod = divmod(num, 10)
            sum += mod
        return sum

    def get_index(nums, num):
        for i, val in enumerate(nums):
            if val == num:
                return i

    def get_sum(nums, num):
        return sum_of_digits(num)

    sorted_nums = sorted(nums, key=lambda num: get_sum(nums, num), reverse=True)

    return sorted_nums

