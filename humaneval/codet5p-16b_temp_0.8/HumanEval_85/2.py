
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    
    even_indices = [x for x in range(len(lst)) if x % 2 == 0]
    new_lst = [lst[i] for i in even_indices if lst[i] % 2 == 0]
    print(sum(new_lst))

