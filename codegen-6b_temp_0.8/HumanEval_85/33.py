
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # initialize a new list called new_lst
    new_lst = []
    # loop through all the elements in lst
    for element in lst:
        # if the index is even, add the element to new_lst
        if element % 2 == 0:
            new_lst.append(element)
    # return new_lst
    return new_lst 

