
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    
    even=[]
    lst_out=[]
    for i in lst:
        if i % 2 == 0 and i not in even:
            lst_out.append(i)
            even.append(i)
    return sum(lst_out)
