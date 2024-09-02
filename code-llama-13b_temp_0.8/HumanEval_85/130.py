
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # # if len(lst) == 0:
    # #     return 0
    # res = 0
    # for idx, val in enumerate(lst):
    #     if idx % 2 == 0 and val % 2 == 0:
    #         res += val
    # return res
    # return sum([x for idx, x in enumerate(lst) if idx % 2 == 0 and x % 2 == 0])
    return sum(lst[::2])
