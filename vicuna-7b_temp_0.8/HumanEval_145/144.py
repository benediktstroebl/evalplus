
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

    # initialize a variable to store the running sum
    current_sum = 0

    # initialize a variable to store the index of the current item
    current_index = 0

    # initialize a variable to store the result
    result = []

    # iterate through the list
    for item in nums:
        # update the running sum
        current_sum += item

        # update the index of the current item
        current_index += 1

        # check if the sum is greater than 9
        if current_sum >= 10:
            # convert the running sum to a single digit number
            current_sum = current_sum % 10
            # check if the current item is greater than the running sum
            if item > current_sum:
                # update the result
                result.insert(current_index - current_sum, item)
                # reset the running sum and the index
                current_sum = 0
                current_index = 0

        # if the current item is greater than the running sum,
        # add it to the result and update the running sum and the index
        else:
            result.append(item)
            current_sum = item

    # if the result is not empty, add the last item to the result
    if result:
        result.append(current_sum)

    # return the result
    return result
