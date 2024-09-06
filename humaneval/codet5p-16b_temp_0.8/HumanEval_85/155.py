
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    new_list = []
    for i in range(len(lst)):
        if i % 2!= 0:
            new_list.append(lst[i])
    return sum(new_list)
