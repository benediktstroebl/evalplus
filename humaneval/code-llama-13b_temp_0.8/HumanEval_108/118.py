
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


    # # def sigDigits(num):
    # #     if num < 0:
    # #         return [num // 10 ** i % 10 for i in range(len(str(num)))]
    # #     return [num // 10 ** i % 10 for i in range(len(str(num)))]
    # #
    # # # Find all positive or negative integers with digits that sum to > 0
    # # # How can we use a list comprehension?
    # #
    # # return len([n for n in arr if sum(sigDigits(n)) > 0])


    # # def sumDigits(num):
    # #     if num < 0:
    # #         return sum([n for n in list(str(num))[1:]])
    # #     return sum([n for n in list(str(num))])
    # #
    # # return len([n for n in arr if sumDigits(n) > 0])


    # # # Get abs values
    # # # Get sum of digits
    # # # If positive, check if digits sum to positive number
    # # # If negative, check if digits sum to negative number
    # #
    # # return len([n for n in arr if sum([int(n) // 10 ** i % 10 for i in range(len(str(n)))]) > 0])


    # # # Use sum() built-in function
    # # return len([n for n in arr if sum([int(n) // 10 ** i % 10 for i in range(len(str(n)))]) > 0])


    # # if arr == []:
    # #     return 0
    # # else:
    # #     return len([n for n in arr if sum([int(n) // 10 ** i % 10 for i in range(len(str(n)))]) > 0])


    return 0
