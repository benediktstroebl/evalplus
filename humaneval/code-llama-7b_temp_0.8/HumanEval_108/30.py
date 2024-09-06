
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
    # 将数组中的负数转换为正数
    arr_new = [abs(i) for i in arr]
    result = []
    for i in arr_new:
        tmp = 0
        while i != 0:
            tmp = tmp * 10 + i % 10
            i = i // 10
        result.append(tmp)
    # 返回数组中符合题意的数的数量
    return len([num for num in result if sum([int(i) for i in str(num)]) > 0])

