
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    lst = [lst[i] for i in range(n//2) if lst[i] % 2 == 0]
    for i in range(n):
        if lst[i] < lst[i+1]:
            lst[i] += lst[i+1]

    return lst