
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
    # define helper function
    def get_digit_sum(num):
        # initialize the counter
        sum_of_digits = 0
        # split the string version of the number into a list of its digits
        digits = list(str(num))
        for digit in digits:
            # for each digit, add it to the counter
            sum_of_digits += int(digit)
        # return the counter
        return sum_of_digits
    # create a new list to store the numbers with their digit sums
    sorted_nums = []
    # iterate through the given list
    for num in nums:
        # for each number, add it to the new list with its digit sum
        sorted_nums.append((get_digit_sum(num), num))
    # sort the new list by the first value of its tuples
    sorted_nums.sort()
    # initialize a new list
    new_nums = []
    # iterate through the sorted list
    for _, num in sorted_nums:
        # for each number, add it to the new list
        new_nums.append(num)
    # return the new list
    return new_nums

