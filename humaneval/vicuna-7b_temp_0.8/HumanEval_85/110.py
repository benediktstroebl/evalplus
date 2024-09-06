
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    odd_indices = [i for i, v in enumerate(lst) if v % 2 != 0]
    for i in odd_indices:
        lst[i], lst[len(lst) - i] = lst[len(lst) - i], lst[i]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
