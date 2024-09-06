
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    if n % 2 == 0:
        result = []
        for i in range(n):
            if i % 2 == 1:
                result.append(lst[i])
        return result
    else:
        result = lst[:]
        for i in range(n//2):
            if i % 2 == 1:
                result.insert(i, result.pop(0))
        return result