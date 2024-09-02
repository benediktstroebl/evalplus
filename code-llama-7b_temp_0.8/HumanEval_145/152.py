
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
    # for each number:  sum_digits = 0
    # while number > 0:
    #   get the last digit of number: % 10
    #   sum_digits += digit
    #   number //= 10
    # if sum_digits in sum_dict:
    #   sum_dict[sum_digits].append(number)
    # else:
    #   sum_dict[sum_digits] = [number]
    # return [x for num in nums for x in sum_dict[sum_points(num)])

    # sort first by number length, then by number value
    # num_len = lambda x: (len(str(x)), x)
    # return sorted(nums, key=num_len)

    # or, first by number length, then by sum of digits
    # num_digits = lambda x: (len(str(x)), sum_points(x))
    # return sorted(nums, key=num_digits)

    # use a dictionary to map from sum of digits to a list of numbers with that sum of digits
    sum_dict = {}
    for number in nums:
        sum_points = sum_digits(number)
        if sum_points in sum_dict:
            sum_dict[sum_points].append(number)
        else:
            sum_dict[sum_points] = [number]
    # we want to return the numbers sorted by original index in nums
    # to do that, we need to add each number's original index to the list in sum_dict
    for number in nums:
        sum_points = sum_digits(number)
        sum_dict[sum_points].append(nums.index(number))
    # now we can sort by key, which will put the numbers in order by the sum of digits
    num_points = lambda x: sum_dict[x]
    sum_points = sorted(sum_dict)
    # now we return the original numbers, but sorted by the index they have in sum_points
    return [nums[sum_dict[point][-1]] for point in sum_points]
