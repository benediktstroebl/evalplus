
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    # TODO: Write your code here
    total = 0
    i = 0
    while i < len(lst):
        if i % 2 == 0 and lst[i] % 2!= 0:
            total += lst[i]
        i += 1
    return total
