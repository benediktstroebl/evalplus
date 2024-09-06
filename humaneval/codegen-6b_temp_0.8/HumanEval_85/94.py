
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # ADD YOUR CODE HERE
    i = 0
    j = 1
    while i < len(lst):
        if j % 2 == 0:
            lst[i] += lst[j]
        i+=1
        j+=1
    return lst


