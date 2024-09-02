
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
    # 1st solution:
    # O(n) time | O(n) space
    # def count_nums(arr):
    #     res = 0
    #     for num in arr:
    #         if sum(map(abs, str(num))) > 0:
    #             res += 1
    #     return res

    # 2nd solution:
    # O(n) time | O(n) space
    # def count_nums(arr):
    #     return sum(map(lambda num: sum(map(abs, str(num))) > 0, arr))

    # 3rd solution:
    # O(n) time | O(n) space
    # def count_nums(arr):
    #     res = 0
    #     for num in arr:
    #         if num < 0:
    #             num *= -1
    #         while num:
    #             num, last_digit = divmod(num, 10)
    #             if last_digit > 0:
    #                 res += 1
    #     return res

    # 4th solution:
    # O(n) time | O(1) space
    # def count_nums(arr):
    #     res = 0
    #     for num in arr:
    #         if num < 0:
    #             num *= -1
    #         while num:
    #             num, last_digit = divmod(num, 10)
    #             if last_digit > 0:
    #                 res += 1
    #     return res

    # 5th solution:
    # O(n) time | O(1) space
    # def count_nums(arr):
    #     return sum(1 for num in arr if num >= 0 and sum(map(abs, str(num))) > 0)

    # 6th solution:
    # O(n) time | O(n) space
    # def count_nums(arr):
    #     return len([num for num in arr if sum(map(abs, str(num))) >
