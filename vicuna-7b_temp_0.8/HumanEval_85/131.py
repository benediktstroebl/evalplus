
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst = list(lst)
    n = len(lst)
    for i in range(n-1):
        if (lst[i] % 2 == 0) and (lst[i+1] % 2 != 0):
            lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
