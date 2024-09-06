
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    odd_index = [i for i in lst if i % 2 != 0]
    if not odd_index:
        return lst
    else:
        even_lst = []
        for i in odd_index:
            even_lst.append(lst[i])
        odd_lst = lst[len(even_lst):]
        return odd_lst[::-1]
