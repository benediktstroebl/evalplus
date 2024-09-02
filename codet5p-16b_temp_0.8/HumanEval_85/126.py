
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    lst2 = []
    for index, element in enumerate(lst):
        if index % 2!= 0:
            lst2.append(element)
    return sum(lst2)
