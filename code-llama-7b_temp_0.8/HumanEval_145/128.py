
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
    def sum_of_digits(num):
        sum = 0
        for digit in str(abs(num)):
            sum += int(digit)
        return sum

    dict = {}
    for i in range(len(nums)):
        dict[nums[i]] = sum_of_digits(nums[i])

    new_dict = sorted(dict.items(), key=lambda x: x[1])
    new_dict_2 = sorted(new_dict, key=lambda x: x[0])
    result = []
    for i in range(len(new_dict_2)):
        result.append(new_dict_2[i][0])

    return result
