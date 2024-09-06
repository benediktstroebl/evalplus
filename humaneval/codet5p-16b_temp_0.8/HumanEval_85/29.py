
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    l = []
    for i, n in enumerate(lst):
        if i%2==0 and n%2==0:
            l.append(n)
    return sum(l)

