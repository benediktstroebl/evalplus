
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    result = []
    i = 0
    while i < len(lst):
        if i%2 !=0:
            if lst[i]%2 == 0:
                result.append(lst[i])
        i +=1
    return sum(result)
