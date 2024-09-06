
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even = []
    for i in range(len(lst)):
        if (lst[i] % 2) == 0:
            even.append(lst[i])
    lst = [x for x in lst if x % 2 != 0]
    for i in range(len(lst)):
        if i % 2 == 1:
            lst[i] = even.pop()
    return lst