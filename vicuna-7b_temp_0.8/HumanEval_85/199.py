
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    i = 0
    while i < len(lst) - 1:
        if lst[i] % 2 == 0:
            # Even element found
            j = i + 1
            while j < len(lst) and lst[j] % 2 == 0:
                j += 1
            # Copy remaining odd elements to the end of the list
            lst[i:j] = lst[i+1:j+1]
            i += 1
    return lst