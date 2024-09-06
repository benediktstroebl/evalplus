
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    new_lst = []
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0 and i % 2 != 0:
            new_lst.append(lst[i])
        i += 1
    print(new_lst)

