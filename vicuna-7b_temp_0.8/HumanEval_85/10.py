
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    even_index = [i for i in range(n) if i % 2 == 0]
    lst[even_index[0]] += lst[even_index[0] + 1]
    return lst