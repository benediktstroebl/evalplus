
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return lst
    else:
        odd_idx = [i for i in range(len(lst)) if i % 2 != 0]
        even_lst = [lst[i] for i in odd_idx]
        lst = [lst[i] for i in range(len(lst)) if i % 2 == 0]
        return odd_lst + even_lst

result = add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
