
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return reduce(lambda x,y: x+y, [lst[i] for i in range(0,len(lst),2) if lst[i]%2==0])
    


