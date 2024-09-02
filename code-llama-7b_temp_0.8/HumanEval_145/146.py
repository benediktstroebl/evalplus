
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

    # My solution:
    #
    # if len(nums) == 0:
    #     return []
    #
    # new_list = []
    #
    # for i in range(len(nums)):
    #     sum_of_digits = 0
    #     for n in str(nums[i]):
    #         sum_of_digits += int(n)
    #     new_list.append([nums[i], sum_of_digits])
    #
    # new_list.sort(key=lambda x: x[1])
    # new_list.sort(key=lambda x: x[0])
    #
    # return [element[0] for element in new_list]

    # My solution 2:
    #
    # if len(nums) == 0:
    #     return []
    #
    # new_list = []
    #
    # for n in nums:
    #     sum_of_digits = 0
    #     for num in str(n):
    #         sum_of_digits += int(num)
    #     new_list.append([n, sum_of_digits])
    #
    # new_list.sort(key=lambda x: (x[0], x[1]))
    # return [element[0] for element in new_list]

    # Simplified version from:
    # https://github.com/ejguan/edabit-from-the-book/blob/master/Chapter%203/Order%20By%20Points.py

    def digits_sum(x):
        return sum([int(d) for d in str(x)])

    def digits_sum_key(x):
        return (digits_sum(x), nums.index(x))

    return sorted(nums, key=digits_sum_key)

