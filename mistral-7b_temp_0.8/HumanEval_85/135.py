
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    count = 0
    new_list = []
    for x in lst:
        count += 1
        if count % 2 != 0 and x % 2 == 0:
            new_list.append(x)
    return sum(new_list)
