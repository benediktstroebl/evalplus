
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    even_lst = [lst[i] if (i % 2) == 0 else lst[i+1] for i in range(n)]
    return lst + even_lst

