
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

    # empty list
    if len(nums) == 0:
        return []

    # create a dictionary
    # key: the sum of digits for each integer in nums
    # value: a list of integers which have the same key
    sum_digits = dict()
    for i, n in enumerate(nums):
        sum_of_digits = 0
        abs_num = abs(n)
        while abs_num:
            sum_of_digits += abs_num % 10
            abs_num //= 10

        if sum_of_digits in sum_digits:
            sum_digits[sum_of_digits].append(n)
        else:
            sum_digits[sum_of_digits] = [n]

    # create a new list
    result = []
    for i, k in enumerate(sorted(sum_digits.keys())):
        for item in sum_digits[k]:
            result.append(item)

    return result

