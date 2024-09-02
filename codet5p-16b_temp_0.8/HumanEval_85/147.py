
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    lst2 = []
    lst3 = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst2.append(lst[i])
    
    for i in range(len(lst2)):
        if i % 2!= 0:
            lst3.append(lst2[i])
    return sum(lst3)

