
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    # create dictionary
    # loop through the list 
    # for each value, check the dictionary to see if it's a key
    # if it is, return that key
    # if it's not a key, add it to the dictionary 
    # do this for all of the numbers
    # keep track of the smallest value 
    # return the next smallest value (use dictionary)
    # if there is no next smallest value, return None
    # create dictionary
    dct = {}
    
    # loop through list
    for i in lst:
        if i in dct.keys():
            return i
        else:
            dct[i] = True
    return None
