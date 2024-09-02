
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst_ = list(lst)
    count = 0
    for i in range(len(lst_)):
        if i % 2 == 0:
            lst_[i] += count
            count += 1
    return
