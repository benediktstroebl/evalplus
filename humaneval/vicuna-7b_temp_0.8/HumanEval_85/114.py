
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    if n%2 == 0:
        return lst
    for i in range(n):
        if i%2 == 1:
            lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst

lst = [6,7,4,2,6,7,4,2]
