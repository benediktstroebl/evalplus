
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    odd_index = []
    for i in range(len(lst)):
        if (i % 2) != 0:
            odd_index.append(i)
    return lst[odd_index]
