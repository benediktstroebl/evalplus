


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
    
    # Part 1: squaring and cubing
    # Get list of indexes of items that are to be squared
    squared_indices = [i for i in range(len(lst)) if i % 3 == 0]
    # Get list of indexes of items that are to be cubed
    cubed_indices = [i for i in range(len(lst)) if i % 4 == 0 and i not in squared_indices]
    # Square the items at those indices
    lst_copy = lst.copy()
    for idx in squared_indices:
        lst_copy[idx] **= 2
    for idx in cubed_indices:
        lst_copy[idx] **= 3
    
    # Part 2: Summing
    return sum(lst_copy)

