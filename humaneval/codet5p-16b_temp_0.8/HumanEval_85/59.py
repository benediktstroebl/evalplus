
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    assert len(lst)>0 and lst.__class__==list, "add expects a non-empty list of integers"
    return sum([lst[2*i] for i in range(len(lst)//2) if lst[2*i]%2==0])

