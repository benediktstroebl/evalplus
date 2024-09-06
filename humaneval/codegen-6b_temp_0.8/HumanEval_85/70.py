
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    #wipe the list by adding 0 to the beginning
    lst = [0] + lst
    #increase the index i by 2 for each item in lst
    i = 1
    while i < len(lst):
        #add 2 to i if the number is even
        lst[i] += 2
        i += 2
    #remove the 0 at the beginning
    del lst[0]
    #return the output
    return lst
