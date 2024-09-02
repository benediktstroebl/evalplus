
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return []
    else:
        odds = lst[:lst.index(lst[1])]
        even_lst = [x for x in odds if x % 2 == 0]
        return even_lst + lst[lst.index(lst[1])+1:]

lst = [4, 2, 6, 7]
