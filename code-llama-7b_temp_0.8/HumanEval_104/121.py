
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    # hash_table = {}

    # for n in x:
    #     num = n
    #     while num != 0:
    #         dig = num % 10
    #         if dig not in hash_table:
    #             hash_table[dig] = 0
    #         num = num // 10

    #     for dig in hash_table.keys():
    #         if dig % 2 == 0:
    #             hash_table[dig] += 1

    # return [n for n in x if sum(map(lambda x: x % 2 == 0, map(int, str(n)))) == 0]

    return [n for n in x if not any(map(lambda x: x % 2 == 0, map(int, str(n))))]

