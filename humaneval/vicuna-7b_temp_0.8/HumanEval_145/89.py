
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
    # check if there are any numbers in the list
    if not nums:
        return []

    # get the sum of all numbers
    total_sum = sum(nums)
    if total_sum < 0:
        raise ValueError("Invalid input")

    # sort the list
    sorted_nums = sorted(nums, key=lambda x: abs(sum(int(x) for x in str(x))), reverse=True)

    # if the list is empty or there is only one number, return it
    if len(sorted_nums) < 2 or len(sorted_nums) == 1:
        return sorted_nums

    # initialize a new list to store the numbers
    # we will only keep the positive numbers and those with higher point value
    positive_numbers = []

    # keep track of the total point value of the numbers
    total_point_value = 0

    # iterate over the sorted list
    for num in sorted_nums:
        # check if num is positive
        if num > 0:
            # add num to the list of positive numbers
            positive_numbers.append(num)
            # update the total point value
            total_point_value += num * abs(sum(int(x) for x in str(num)))

    # if the total_point_value is 0, return an empty list
    if total_point_value == 0:
        return []

    # sort the positive numbers in descending order based on their point value
    positive_numbers = sorted(positive_numbers, key=lambda x: x * abs(sum(int(x) for x in str(x))), reverse=True)

    return positive_numbers