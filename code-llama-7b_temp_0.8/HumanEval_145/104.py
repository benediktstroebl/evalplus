
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
    def get_num_sum(num):
        return sum([int(n) for n in str(num)])

    result = []
    unique_sums = set()

    for num in nums:
        if num not in result and get_num_sum(num) not in unique_sums:
            result.append(num)
            unique_sums.add(get_num_sum(num))

    return sorted(result, key=get_num_sum)

