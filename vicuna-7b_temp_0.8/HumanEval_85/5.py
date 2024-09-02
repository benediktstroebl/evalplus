
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return []
    i = 0
    while i < len(lst):
        if i % 2 == 1:
            even_lst = [x for x in lst if x % 2 == 0]
            if even_lst:
                lst.insert(i+1, even_lst[0])
                even_lst.pop(0)
                return lst
        i += 1
    return []

lst = [1, 2, 3, 4, 5]
print(add(lst))
