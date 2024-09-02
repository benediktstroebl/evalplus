
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    
    lst_out = []
    for index, element in enumerate(lst):
        if index % 2!= 0 and element % 2 == 0:
            lst_out.append(element)
    return sum(lst_out)

