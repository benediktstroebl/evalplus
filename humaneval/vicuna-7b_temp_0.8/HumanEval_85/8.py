
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_lst = [i for i in lst if i % 2 == 0]
    odd_lst = lst[1:len(lst) - 1]
    even_lst.insert(0, odd_lst[::2])
    return even_lst[::2]