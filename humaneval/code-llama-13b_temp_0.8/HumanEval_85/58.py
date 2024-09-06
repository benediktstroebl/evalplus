
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    evens = [num for i, num in enumerate(lst) if num%2 == 0 and i%2 == 0]
    return sum(evens)
    
