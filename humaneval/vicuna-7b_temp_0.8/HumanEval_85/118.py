
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_lst = []
    for i in range(len(lst)):
        if i%2==1:
            even_lst.append(lst[i])
    return even_lst
