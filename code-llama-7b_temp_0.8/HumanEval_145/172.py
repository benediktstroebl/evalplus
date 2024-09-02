
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

    # First we have to transform the list of numbers into a list of tuples
    # in which the number is transformed into a tuple (sum of its digits, number)
    result = []
    for i in nums:
        result.append((sum([int(j) for j in str(i)]), i))

    # Now, let's sort the list of tuples based on their first element
    result.sort(key=lambda x: x[0])

    # The result is a list of tuples, so we have to go back to a list of numbers
    # by keeping only the second element of the tuples
    return [x[1] for x in result]

