
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    
    return sum([x for x in lst if x%2==0 and lst.index(x)%2!=0])


