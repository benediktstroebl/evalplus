
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    new_list = []
    i = 0
    while i < len(lst):
        if i % 2 == 0 and lst[i] % 2 == 0:
            new_list.append(lst[i])
        i += 1
    return sum(new_list)
