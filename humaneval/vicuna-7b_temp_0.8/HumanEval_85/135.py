
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    for i in range(len(lst)):
        if i % 2 == 1:
            lst[i], lst[i+1] = lst[i+1], lst[i]

lst = [7, 6, 4, 2, 8, 1, 9, 3, 5]
add(lst)
