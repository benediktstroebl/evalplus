
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_list = lst[::2]
    odd_list = lst[1::2]
    odd_list = list(filter(lambda x: x % 2 == 0, odd_list))
    return sum(odd_list)
