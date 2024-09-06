
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    odds = [i for i, x in enumerate(lst) if x % 2 != 0]
    even_lst = [lst[i] for i in odds]
    lst = [lst[i] for i in range(len(lst)) if i not in odds]
    result = [lst[i] if i % 2 == 0 else even_lst[0] for i in range(len(lst))]
    return result
