
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_odd = [lst[i] if i % 2 == 1 else None for i in range(len(lst))]
    return sum([lst[i] for i in range(len(lst)) if even_odd[i] is not None])


