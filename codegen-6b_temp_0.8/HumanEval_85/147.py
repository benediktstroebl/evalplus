
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # for i in range(len(lst)):
    #     if i % 2:
    #         lst[i] = lst[i] - 1
    # return lst
    return [i - 1 for i in lst if i % 2]
