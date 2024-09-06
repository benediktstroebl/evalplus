


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
    # checking if lst is empty
    if not lst:
        return 0
    
    # checking if lst is a single number
    if not isinstance(lst, list):
        return int(lst)**2
    
    # get all indexes of multiples of 3 and 4
    indices = [i for i, x in enumerate(lst) if x % 3 == 0 or x % 4 == 0]
    
    # calculate the sum of all squared entries
    sum = 0
    for i in indices:
        sum += lst[i]**2
    
    # calculate the sum of all cubed entries
    for i in indices:
        sum += lst[i]**3
    
    return sum
