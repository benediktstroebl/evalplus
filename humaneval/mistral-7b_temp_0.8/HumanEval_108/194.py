
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

    arr_count = 0

    for i in arr:
        i = str(i)

        if i[0] == '-':
            for j in range(len(i)-1):
                if i[j] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    arr_count += 1
                else:
                    pass

        else:
            for j in range(len(i)):
                if i[j] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    arr_count += 1
                else:
                    pass

    return arr_count

