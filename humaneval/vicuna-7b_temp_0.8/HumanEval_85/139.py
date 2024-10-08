
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    for i in range(len(lst)):
        if(lst[i]%2 == 0 and lst[i] != 0):
            lst[i-1],lst[i] = lst[i],lst[i-1]
        elif(lst[i]%2 == 0):
            lst[i-1] += lst[i]
    return lst