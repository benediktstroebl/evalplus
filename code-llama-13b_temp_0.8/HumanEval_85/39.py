
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # init
    output = 0
    # main
    if len(lst) > 0:
        output = lst[1] if lst[0]%2 == 0 else 0
    if len(lst) > 2:
        output += lst[3] if lst[2]%2 == 0 else 0
        i = 4
        while i < len(lst):
            output += lst[i] if lst[i-1]%2 == 0 else 0
            i += 2
    # return
    return output



