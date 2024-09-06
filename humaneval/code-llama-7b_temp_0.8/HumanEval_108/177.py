
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

    # my solution
    # def count_nums(arr):
    #     result = 0
    #     for element in arr:
    #         if sum(int(x) for x in str(abs(element))) > 0:
    #             result += 1
    #     return result

    # my solution 2
    # def count_nums(arr):
    #     result = 0
    #     for element in arr:
    #         result += sum(int(x) for x in str(abs(element))) > 0
    #     return result

    # pythonic solution
    # return len([x for x in arr if sum(int(y) for y in str(abs(x))) > 0])

    # return sum(sum(int(x) for x in str(abs(x))) > 0 for x in arr)

    # pythonic solution 2
    return len([int(x) for x in str(sum(arr)) if int(x) > 0])

