
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    i = 0
    even_lst = []
    for num in lst:
        if num % 2 == 0:
            even_lst.append(num)
            lst.remove(num)
            i += 1
        else:
            i += 1
    return even_lst

