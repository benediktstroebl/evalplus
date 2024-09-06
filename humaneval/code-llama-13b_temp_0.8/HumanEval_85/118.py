
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if len(lst) == 0:
        raise Exception("Given list is empty")
    else:
        i = 0
        sum = 0
        while(i < len(lst)):
            if (lst[i] % 2 == 0):
                sum = sum + lst[i]
            i += 2
        return sum

