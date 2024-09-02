
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return None
    else:
        sum_lst = 0
        for i in range(len(lst)):
            if i % 2 == 1:
                sum_lst += lst[i]
        return sum_lst
        
