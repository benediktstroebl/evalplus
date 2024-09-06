
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_index = [i for i, x in enumerate(lst) if x % 2 == 0]
    new_lst = []
    for i in range(len(lst)):
        if i in even_index:
            new_lst.append(lst[i])
        else:
            new_lst.append(lst[i])
    return new_lst