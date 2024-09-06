
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
    # your code here
    # When there are duplicates, we need to order them by their index
    # in the original list. So, we use a dict to keep track of
    # a list of indices for each sum
    # Then, we sort by this dict, and map the result to the original list

    nums_dict = {}

    for i, num in enumerate(nums):
        # find sum of digits
        num_str = str(num)
        sum = 0
        for c in num_str:
            sum += int(c)

        if sum not in nums_dict:
            nums_dict[sum] = [i]
        else:
            nums_dict[sum].append(i)

    # reverse mapping
    res = [0 for _ in nums]
    for num in nums_dict:
        lst = nums_dict[num]
        lst.reverse()
        for i, idx in enumerate(lst):
            res[idx] = num * (i + 1)

    return res

