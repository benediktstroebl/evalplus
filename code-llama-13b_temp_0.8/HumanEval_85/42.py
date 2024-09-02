
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # write code here
    return sum([lst[i] for i in range(0, len(lst), 2) if i%2==1])
