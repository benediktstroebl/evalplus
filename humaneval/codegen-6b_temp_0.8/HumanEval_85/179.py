
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    def even_at_odd(lst):
        while len(lst) >= 1:
            if lst[0] % 2 == 0:
                return lst.pop(0)
            else:
                return lst.pop(0)
    num_added = 0
    for i in range(len(lst)):
        num_added += even_at_odd(lst)
        if i % 2 == 1:
            num_added += 1
    return num_added

