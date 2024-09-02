
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if lst == []:
        return None
    if len(lst) == 0:
        return None
    result = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    return sum(result)
