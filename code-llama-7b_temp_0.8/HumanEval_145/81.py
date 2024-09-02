
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
    nums_ordered = []
    nums_ordered_by_index = []

    # Remove all negative values
    nums = list(filter((lambda x: x > 0), nums))

    # Calculate the sum of digits for each value
    nums_sums = [sum(int(d) for d in str(i)) for i in nums]

    # Generate a list of tuples, with each tuple having the following structure
    # (original_index, sum_of_digits, original_value)
    ordered_nums = list(zip(range(len(nums)), nums_sums, nums))

    # Sort the tuples using the sum of digits in ascending order,
    # then use the original_index as a tiebreaker
    ordered_nums.sort(key=lambda tup: (tup[1], tup[0]))

    # Add the original values to the return list
    nums_ordered = [tup[2] for tup in ordered_nums]

    return nums_ordered

