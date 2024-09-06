
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst = [2*lst[i] for i in range(len(lst)) if i%2==1]
    return sum(lst)

