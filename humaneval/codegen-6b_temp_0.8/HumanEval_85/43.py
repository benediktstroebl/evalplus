
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    i = 0
    lenght = len(lst)
    while i < lenght:
        if lst[i] % 2 == 0:
            lst.insert(i+1,lst[i])
            lst.pop(i)
        else:
            i+=1
    return lst
