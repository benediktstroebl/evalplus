
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # --- 1st Solution ---
    return sum([lst[i] for i in range(len(lst)) if i % 2 == 0])

    # --- 2nd Solution ---
    # return reduce(lambda x, y: x + y, lst[::2])

