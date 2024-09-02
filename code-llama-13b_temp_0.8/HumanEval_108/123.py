
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    # PLAN
    # - init a counter variable, set to 0
    # - iterate over arr
    # - for each element
    #   - convert to a string
    #   - convert to a list of digits
    #   - if the sum of the list is > 0, add 1 to counter
    # - return counter

    counter = 0
    for num in arr:
        string_of_num = str(num)
        list_of_nums = [int(x) for x in string_of_num]
        if sum(list_of_nums) > 0:
            counter += 1
    return counter


    # OTHER SOLUTION
    # PLAN
    # - init a counter variable, set to 0
    # - iterate over arr
    # - for each element
    #   - if the number is negative, make positive
    #   - get the last digit of the number
    #   - get the sum of all digits
    #   - if sum of digits is > 0, add 1 to counter
    # - return counter

    # counter = 0
    # for num in arr:
    #     if num < 0:
    #         num *= -1
    #     last_digit = num % 10
    #     sum_of_digits = 0
    #     while num > 0:
    #         sum_of_digits += num % 10
    #         num = num // 10
    #     if sum_of_digits > 0:
    #         counter += 1
    # return counter
