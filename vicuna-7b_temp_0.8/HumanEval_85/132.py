
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    odd_idx = [idx for idx, x in enumerate(lst) if x % 2 != 0]
    even_lst = [lst[idx] for idx in odd_idx]
    lst = [x + y for x, y in zip(lst[odd_idx], even_lst)]
    return lst

lst = [3, 5, 6, 7, 8, 10]
print(add(lst))
