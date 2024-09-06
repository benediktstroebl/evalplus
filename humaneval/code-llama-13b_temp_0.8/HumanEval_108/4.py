
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

    # Solution 1: 40 chars
    # return len([n for n in arr if sum([int(d) for d in str(n)]) > 0])

    # Solution 2: 42 chars
    # return len(list(filter(lambda n: sum([int(d) for d in str(n)]) > 0, arr)))

    # Solution 3: 33 chars
    return len([x for x in arr if sum(map(int, str(x))) > 0])

    # Solution 4: 32 chars
    # return len(list(filter(lambda x: sum(map(int, str(x))) > 0, arr)))

    # Solution 5: 33 chars
    return sum(1 for x in arr if sum(map(int, str(x))) > 0)

    # Solution 6: 27 chars
    # return sum(map(lambda x: sum(map(int, str(x))) > 0, arr))

    # Solution 7: 28 chars
    # return sum(map(lambda x: sum(map(int, str(x))) > 0, arr))

    # Solution 8: 26 chars
    # return sum(map(int, str(x)) > 0 for x in arr)
