
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    # Write your code here.
    add_even_num = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            add_even_num += lst[i]
    return add_even_num

