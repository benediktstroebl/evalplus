
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    """ALGORITHM"""
    # # iterate through list, adding even numbers at odd indices
    # for i in range(len(lst)):
    #     if i % 2!= 0:
    #         lst[i] += lst[i - 1]
    #     else:
    #         pass

    # # return sum of all even indices
    # return lst[::2]

    # # iterate through list, adding even numbers at odd indices
    # sum = 0
    # for i in range(len(lst)):
    #     if i % 2!= 0:
    #         sum += lst[i]
    #     else:
    #         pass
    # return sum

    # more concise
    return sum([x for i, x in enumerate(lst) if i % 2!= 0])
