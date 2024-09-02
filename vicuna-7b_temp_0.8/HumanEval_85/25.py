
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if len(lst) < 2:
        return lst
    else:
        odd_idx = [i for i, x in enumerate(lst) if x % 2 != 0]
        even_lst = [x for i, x in enumerate(lst) if i % 2 == 0]
        for i, x in enumerate(odd_idx):
            lst[i:i+2] = even_lst[i]
        return lst

lst = [3, 6, 7, 1, 2, 4, 5, 8, 9, 10]
print(add(lst))
