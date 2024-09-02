
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_lst = []
    i = 0
    for num in lst:
        if i % 2 == 0:
            even_lst.append(num)
            i += 1
        else:
            even_lst.append(num)
            i += 1
    return even_lst

