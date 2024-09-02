
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
    # Hints:
    # 1. Think about the algorithm first.
    # 2. Try out several cases by hand.
    # 3. Develop the algorithm in a top-down manner.

    # Plan:
    # 1. Sort the array by each number of digits
    # 2. Sort the array by each digit
    # 3. Sort the array by the index

    def digits(num):
        return [int(x) for x in str(num)]
    def digit_sum(num):
        return sum(digits(num))

    new_nums = sorted(nums, key=digit_sum)
    new_nums = sorted(new_nums, key=lambda x: digits(x))
    new_nums = sorted(new_nums, key=nums.index)
    return new_nums
