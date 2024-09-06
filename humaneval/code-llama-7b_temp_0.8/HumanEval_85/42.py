
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    new_lst = []
    for i in range(len(lst)):
        if i % 2 == 1:
            new_lst.append(lst[i])
    
    s = 0
    for num in new_lst:
        s += num
    return s

