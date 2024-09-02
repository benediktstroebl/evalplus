
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    evens = []
    for num in lst:
        if (num % 2) == 0:
            evens.append(num)
    
