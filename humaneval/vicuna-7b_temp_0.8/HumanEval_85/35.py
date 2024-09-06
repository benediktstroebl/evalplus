
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_index = [i for i, x in enumerate(lst) if x % 2 == 0]
    return [lst[i] for i in even_index]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
