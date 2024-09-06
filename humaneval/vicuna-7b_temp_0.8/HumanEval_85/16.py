
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    odd_idx = [i for i, x in enumerate(lst) if x % 2 != 0]
    even_lst = [lst[i] for i in odd_idx]
    result = [lst[i] for i in odd_idx]
    result += even_lst
    return result