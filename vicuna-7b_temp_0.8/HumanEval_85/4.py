
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_index = [(i+1) % 2 for i in range(len(lst))]
    even_lst = [lst[i] for i in even_index]
    return lst[even_index] + sum(even_lst)
