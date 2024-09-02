
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    even_lst = [lst[i] for i in range(n//2+1) if lst[i] % 2 == 0]
    odd_lst = [lst[i] for i in range(n//2) if lst[i] % 2 != 0]
    for i in range(n):
        lst[i] = even_lst[i]
    return lst