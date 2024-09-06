
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            total += lst[i]
    return total
