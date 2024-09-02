
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    new_list = []
    for index in range(len(lst)):
        if lst[index] % 2 == 0 and index % 2 == 1:
            new_list.append(lst[index])
    return new_list
