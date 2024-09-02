
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    if n % 2 == 0:
        lst.insert(0, lst[0])
        lst.insert(1, lst[1])
    i = 0
    for j in range(n-1):
        if lst[j] % 2 == 0:
            lst[i] += lst[j+1]
            i += 1
            lst.remove(lst[j])
    return lst