


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
    # Check if the list is not empty
    if not lst:
        return 0
    
    # Create a new list to store the squared and cubed entries
    squared = []
    cubed = []
    
    # Iterate through the list
    for i in range(len(lst)):
        if i % 3 == 0:
            # If the index is a multiple of 3, square the entry
            squared.append(lst[i]**2)
        elif i % 4 == 0:
            # If the index is a multiple of 4, cube the entry
            cubed.append(lst[i]**3)
        else:
            # If the index is not a multiple of 3 or 4, don't change the entry
            lst[i] = lst[i]
    
    # Concatenate the squared and cubed entries to a single list
    return sum(squared) + sum(cubed)

