
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    odd_indices = [i for i in range(len(lst)) if i%2 == 1]
    even_lst = [lst[i] for i in odd_indices]
    lst = [lst[i] for i in range(len(lst)) if i%2 == 0]
    for i in odd_indices:
        lst.append(even_lst.pop())
    return lst
