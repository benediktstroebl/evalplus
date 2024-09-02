
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return []
    n = len(lst)
    even = 0
    for i in range(n-1):
        if lst[i] % 2 == 0:
            even += lst[i]
        else:
            lst[i] = lst[i] + 1
            even += 2
    return [lst[i] for i in range(n-1) if lst[i] % 2 == 0] + [even]

lst = add([4, 2, 6, 7, 3, 5, 10, 11, 8, 9])
