
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    """Now here we are adding the even elements at odd indices..
    
    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    new_list = []
    for i in lst:
        if i % 2 == 0:
            if i not in new_list:
                new_list.append(i)

    return new_list

