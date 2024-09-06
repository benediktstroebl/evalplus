
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    if len(lst) == 0:
        return 0
    else:
        even_indices = [i for i in range(len(lst)) if lst[i] % 2 == 0 and i % 2!= 0]
        return sum([lst[i] for i in even_indices])

