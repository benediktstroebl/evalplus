
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
    # My solution
    # sorted_list = []
    # for num in nums:
    #     sum_digits = sum([int(digit) for digit in str(abs(num))])
    #     if not sorted_list:
    #         sorted_list.append(num)
    #     else:
    #         for i in range(len(sorted_list)):
    #             if sum_digits < sum_digits:
    #                 sorted_list.insert(i, num)
    #                 break
    #             elif sum_digits > sum_digits:
    #                 sorted_list.append(num)
    #                 break
    #             elif sum_digits == sum_digits and i == len(sorted_list) - 1:
    #                 sorted_list.append(num)
    # return sorted_list

    # https://www.geeksforgeeks.org/sort-list-according-to-the-sum-of-their-digits/
    def digitsum(n):
        return sum(map(int, str(n)))

    def get_sum_dict(nums):
        d = {}
        for num in nums:
            if num not in d:
                d[num] = digitsum(num)
        return d

    def custom_key(num):
        return (sum_dict[num], num)

    sum_dict = get_sum_dict(nums)
    return sorted(nums, key=custom_key)

