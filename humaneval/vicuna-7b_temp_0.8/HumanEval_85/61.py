
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst.sort(key=lambda x: x % 2 == 0)
    result = []
    for i in range(len(lst)):
        if i % 2 == 1:
            result.append(lst[i])
        result.append(0)
    return result

