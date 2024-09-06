
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    i = 1
    newlst = []
    while i < len(lst) :
        if i%2 == 1 and lst[i]%2 == 0:
            newlst.append(lst[i])
        i += 1
    return newlst
    
