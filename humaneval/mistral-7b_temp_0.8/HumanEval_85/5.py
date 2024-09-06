
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    print(sum(l for l in lst if (l % 2 == 0 and lst.index(l) % 2 == 1)))

