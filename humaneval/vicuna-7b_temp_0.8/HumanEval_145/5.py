
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
    # sort the list
    nums = sorted(nums)

    # initialize variables to store the index of the number in the original list
    # and the number itself
    index = [nums.index(num) for num in nums]
    numbers = [num for i, num in enumerate(nums) if i not in index]

    # calculate sum of digits of each number
    sums = [sum(int(num) for num in str(num)) for num in numbers]

    # store numbers in the original list with the highest sum of digits first
    return sorted(numbers, key=lambda x: sums.index(max(sums, key=sums.get)))
