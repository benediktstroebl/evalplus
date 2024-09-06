


def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    # Check if the input list is empty
    if not lst:
        return 0
    
    # Check if the input list is not empty
    if len(lst) == 1:
        return lst[0]**2
    
    # Check if the input list is not empty
    if len(lst) == 2:
        if (lst[0]-lst[1])**2 not in (lst[0]*lst[1]*lst[0], lst[0]*lst[1]*lst[1]):
            return 0
        return lst[0]*lst[1]*lst[0] + lst[0]*lst[1]*lst[1]
    
    # Check if the input list is not empty
    for i in range(2, len(lst)):
        if (lst[i-1]-lst[i])**2 not in (lst[i-1]*lst[i]*lst[i-1], lst[i-1]*lst[i]*lst[i]):
            return 0
        if lst[i-1]*lst[i] not in (lst[i-1]*lst[i]*lst[i], lst[i-1]*lst[i]*lst[i]):
            return 0
        if (lst[i-2]-lst[i])**2 not in (lst[i-2]*lst[i]*lst[i-2], lst[i-2]*lst[i]*lst[i-2]):
            return 0
        if lst[i-2]*lst[i] not in (lst[i-2]*lst[i]*lst[i], lst[i-2]*lst[i]*lst[i]):
            return 0
        if (lst[i-3]-lst[i])**2 not in (lst[i-3]*lst[i]*lst[i-3], lst[i-3]*lst[i]*lst[i-3]):
            return 0
        if lst[i-3]*lst[i] not in (lst[i-3]*lst[i]*lst[i], lst[i-3]*lst[i]*lst[i]):
            return 0
        
    return lst[0]*lst[
