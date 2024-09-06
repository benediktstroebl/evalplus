
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
    # take the sum of all elements in the list
    total = sum(nums)

    # keep track of the index of each element
    indices = [i for i, num in enumerate(nums)]

    # sort the indices
    sorted_indices = sorted(indices)

    # sort the numbers by their index and the sum of their digits
    nums = [nums[i] for i in sorted_indices]
    for i in range(len(nums)):
        num = nums[i]
        while num > 0:
            digit = num % 10
            num /= 10
            if digit < total / 10:
                break
        else:
            nums[i] = -nums[i]
            total -= num

    return nums
