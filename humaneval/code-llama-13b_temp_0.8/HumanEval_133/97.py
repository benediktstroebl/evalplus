

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    
    # first we need to round each element to the upper int
    # we could just apply the ceiling to the whole list, but it is also 
    # possible to round one number at a time
    
    # this is a for loop
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    
    # we could convert the list to set, but it is important to preserve
    # the order
    
    # square the elements of the list
    for i in range(len(lst)):
        lst[i] **= 2
    
    # return the sum
    return sum(lst)
    
    
    
