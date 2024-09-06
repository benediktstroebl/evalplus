
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    even_lst = []
    for i in range(n // 2):
        if lst[i] % 2 == 0:
            even_lst.append(lst[i])
    for i in range(n // 2, n):
        even_lst.append(lst[i])
    return even_lst

lst = [4, 2, 6, 7, 1, 8, 9]
