
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Your code here
    if len(lst)%2==0:
        return lst[0]+lst[-1]
    else:
        return lst[0]
