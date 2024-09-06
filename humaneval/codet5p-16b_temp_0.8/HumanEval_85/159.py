
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    new_lst = []
    for idx, num in enumerate(lst):
        if idx % 2 == 1:
            if num % 2 == 0:
                new_lst.append(num)

    return sum(new_lst)
