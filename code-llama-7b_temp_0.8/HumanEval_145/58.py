
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
    # Step 1: Write a function which sorts the given list of integers
    # in ascending order according to the sum of their digits.
    def get_sum(nums):
        sum_total = 0
        for num in nums:
            sum_total = sum_total + sum(map(int, list(str(num))))
        return sum_total

    # Step 2: Write a function which sorts the given list of integers
    # in ascending order according to their index in original list.
    def get_index(nums):
        index_total = 0
        for num in nums:
            index_total = index_total + nums.index(num)
        return index_total

    # Step 3: Sort the given list of integers in ascending order
    # according to their index and then according to the sum
    # of their digits.
    return sorted(nums, key=lambda n: (get_sum(nums), get_index(nums)))

