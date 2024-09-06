
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    """ALGORITHM"""
    # # iterate through lst, adding the even elements that are at odd indices
    # for i in range(len(lst)):
    #     if i%2 == 0:
    #         lst[i] += 1

    # # return the sum of the new list
    # return sum(lst)

    """ALGORITHM"""
    # # iterate through lst, adding the even elements that are at odd indices
    # for i in range(1, len(lst), 2):
    #     lst[i] += lst[i-1]

    # # return the sum of the new list
    # return lst[-1]

    """ALGORITHM"""
    return sum(lst[1::2])
