
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    if(len(lst) <= 1):
        return lst
    lst = [lst[i] for i in range(len(lst)) if (i%2==0) and lst[i] % 2==0] # even indices in list
    return add(lst)
