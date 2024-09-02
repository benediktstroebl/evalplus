
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    new_list = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            new_list.append(lst[i])
        else:
            pass
    print(new_list)
    print(sum(new_list))
    return sum(new_list)

