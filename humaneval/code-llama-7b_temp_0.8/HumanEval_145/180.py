
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
    # set up the original list
    list_of_numbers = [num for num in nums]

    # set up a list of tuples with the sum of the digits for each number
    list_of_tuples = [(num, sum(int(d) for d in str(num))) for num in list_of_numbers]

    # sort the list of tuples in order of sum of digits, then by original index
    list_of_tuples.sort(key = lambda x: (x[1], x[0]))

    # return the original numbers in the correct order
    return [num for (num, _) in list_of_tuples]
