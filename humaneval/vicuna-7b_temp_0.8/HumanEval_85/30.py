
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return lst
    result = []
    for i in range(len(lst)):
        if i % 2 == 1:
            result.append(lst[i])
    return result

lst = [5, 2, 6, 7, 8, 9, 10]
lst = add(lst)
