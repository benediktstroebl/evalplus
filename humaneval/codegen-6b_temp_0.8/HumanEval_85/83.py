
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    length = len(lst)
    index = 0
    
    while index < length:

        if index % 2 == 0:
            lst[index] += lst[index + 1]
            index += 2
        else:
            index += 1
            
    return lst[0] if length == 1 else lst

