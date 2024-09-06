
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    count = 1
    n = len(lst)
    for i in lst:
        if count % 2 == 1:
            print(i)
        count += 1
    return





