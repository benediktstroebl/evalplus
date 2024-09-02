
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if lst == []:
        return None
    new_lst = []
    for i in range(0, len(lst)):
        if i % 2 == 1:
            new_lst.append(lst[i])
    return sum(new_lst)



