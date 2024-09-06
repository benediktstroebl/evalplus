
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_list = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and i % 2 == 1:
            even_list.append(lst[i])
    return sum(even_list)

