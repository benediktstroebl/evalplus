
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # your code here
    return sum([i for i in lst if i % 2 == 0 and lst.index(i) % 2 != 0])
