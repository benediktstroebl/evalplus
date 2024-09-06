
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
    # best way:
    # return sum(arr[i] for i in range(len(arr)) if sum(map(abs, str(arr[i]))) > 0)

    # best way:
    # return sum(map(lambda i: sum(map(abs, str(i))) > 0, arr))
    
    # my way:
    # count = 0
    # for i in arr:
    #     new_i = i
    #     while new_i > 0:
    #         if new_i % 10 < 0:
    #             count += 1
    #         new_i //= 10
    # return count

    # my way 2:
    # count = 0
    # for i in arr:
    #     count += i > 0
    #     num = 1
    #     while i > 0:
    #         count += (i % 10 > 0)
    #         i = i // 10
    # return count

    # my way 3:
    # count = 0
    # for i in arr:
    #     while i > 0:
    #         count += (i % 10 > 0)
    #         i = i // 10
    # return count

    # my way 4:
    # count = 0
    # for i in arr:
    #     while i > 0:
    #         if i % 10 > 0:
    #             count += 1
    #         i = i // 10
    # return count

    # my way 5:
    # count = 0
    # for i in arr:
    #     new_i = i
    #     while new_i > 0:
    #         if new_i % 10 > 0:
    #             count += 1
    #         new_i = new_i // 10
    # return count

    # my way 6:
    # count = 0
    # for i in arr:
    #     while i > 0:
    #         if i
