
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_odd_indexes = list(zip(lst[::2], range(len(lst[::2]))))
    print(even_odd_indexes)
    return sum([x for x, i in even_odd_indexes if i % 2 == 0])

