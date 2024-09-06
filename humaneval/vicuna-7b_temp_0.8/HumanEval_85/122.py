
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    for i in range(len(lst)):
        if (lst[i] % 2) == 0:
            # swap with the next element
            lst[i], lst[lst[i] // 2] = lst[lst[i] // 2], lst[i]
            # print(lst)
    return lst

lst = [4, 2, 6, 7, 2, 8]
