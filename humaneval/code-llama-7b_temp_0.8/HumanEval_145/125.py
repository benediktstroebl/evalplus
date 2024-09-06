
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

    if not nums:
        return []

    result = [nums.pop(0)]

    while nums:
        best_num = None
        best_num_value = float('-inf')

        for num in nums:
            num_value = sum(int(n) for n in str(num))
            if num_value > best_num_value:
                best_num = num
                best_num_value = num_value

        result.append(best_num)
        nums.remove(best_num)

    return result

