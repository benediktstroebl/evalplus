
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    even = [lst[i] for i in range(n//2) if not (i%2 == 0)]
    odd = [lst[i] for i in range(n//2) if i%2 == 0]
    lst.extend(even)
    return lst