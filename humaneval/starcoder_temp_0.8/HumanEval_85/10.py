
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_indices = [idx for idx in range(len(lst)) if idx % 2 == 0]
    even_elems = [lst[idx] for idx in even_indices]
    return sum(even_elems)
