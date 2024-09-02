
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    evens = []
    for i, x in enumerate(lst):
        if i % 2 == 0 and x % 2 == 0:
            evens.append(x)
    return sum(evens)
    
