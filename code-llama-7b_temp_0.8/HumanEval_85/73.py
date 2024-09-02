
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_sum = 0
    for i in range(0, len(lst), 2):
        if i % 2 == 1:
            even_sum += lst[i]
    return even_sum

