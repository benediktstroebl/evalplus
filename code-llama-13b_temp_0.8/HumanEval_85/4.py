
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return 0
    odd = []
    even = []
    for i in range(0, len(lst)):
        if i % 2 == 1:
            even.append(lst[i])
        else:
            odd.append(lst[i])
    if odd:
        return sum(even)
    return sum(odd)

