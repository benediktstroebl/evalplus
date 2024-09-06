


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
    # Check if the list is empty
    if not lst:
        return 0
    
    # Iterate over the list
    for item in lst:
        # Determine the index of the item
        index = item
        # Determine the modulus of the index
        mod = 3 if (index % 3 == 0) else 4
        
        # Determine the operation to perform on the item
        op = '**%d' % (mod) if (index % mod) == 0 else '**%d' % mod
        
        # Perform the operation on the item and store the result
        result = eval(op, {'**': lambda x: x**2 if x%2==0 else x**3})(item)
        
        # Add the result to the sum
        sum += result
    
    return sum
