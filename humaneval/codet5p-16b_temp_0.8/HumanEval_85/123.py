
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    counter = 0
    total = 0
    while counter < len(lst):
        if counter % 2 == 0 and lst[counter] % 2 == 0:
            total += lst[counter]
        counter += 1
    return total
