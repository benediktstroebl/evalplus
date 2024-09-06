

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
    # first we need to round up the numbers in the list
    rounded_list = list()
    for x in lst:
        if x > 0:
            rounded_list.append(math.ceil(x))
        elif x < 0:
            rounded_list.append(math.floor(x))
        else:
            rounded_list.append(0)
    
    # now we need to sum the squares
    squared_sum = 0
    for y in rounded_list:
        squared_sum += y**2
    
    return squared_sum
        
        
    
