
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
    # sort the input list
    nums = sorted(nums)

    # initialize a variable to hold the sum of digits for the last item
    last_sum = None

    # initialize a variable to hold the index of the last item
    last_idx = len(nums) - 1

    # iterate through the input list
    for i in range(len(nums)):
        # check if the current item has a leading digit of 1
        if nums[i] == 1:
            # add the current item to the result
            result.append(nums[i])

            # set the sum of digits for the last item
            if last_sum is None:
                last_sum = 0
            last_sum = last_sum + (i + 1) % 10

            # update the last index
            last_idx = i

        # check if the current item has a leading digit of -1
        elif nums[i] == -1:
            # add the current item to the result
            result.append(nums[i])

            # set the sum of digits for the last item
            if last_sum is None:
                last_sum = 0
            last_sum = (i + 1) % 10 + (last_sum + 1) % 10

            # update the last index
            last_idx = i

        # check if the current item has a leading digit of 11 or 12
        elif (nums[i] - 1) in [11, 12]:
            # add the current item to the result
            result.append(nums[i])

            # update the sum of digits for the last item
            if last_sum is None:
                last_sum = 0
            last_sum = (last_sum + (i - 1) % 10) % 10

            # update the last index
            last_idx = i

    # append the remaining items to the result, if any
    if last_sum is None:
        result.append(nums[-1])
    else:
        result.append(last_sum)

    
