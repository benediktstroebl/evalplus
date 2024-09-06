
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
    def sum_of_digits(num):
        sum = 0
        while num > 0:
            digit = num % 10
            num = num // 10
            sum += digit
        return sum

    new_list = []
    for i in nums:
        new_list.append((sum_of_digits(i), i))
    new_list = sorted(new_list, key=lambda x: x[0], reverse=True)
    for i in range(len(nums)):
        if new_list[i][1] == nums[i]:
            new_list.pop(i)
    return [i[1] for i in new_list]


