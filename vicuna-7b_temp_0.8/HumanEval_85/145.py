
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    halfway = len(lst) // 2
    lst_even = [lst[2*i] for i in range(len(lst))]
    lst_odd = [lst[2*i+1] for i in range(len(lst))]
    if len(lst_odd) % 2 == 1:
        odd_lst = lst_odd[:-1]
        even_lst = lst_even + odd_lst
    else:
        odd_lst = lst_odd
        even_lst = [lst[2*i] for i in range(len(lst))]
    lst = [x for x in even_lst if x % 2 == 0]
    return lst
