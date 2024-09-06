


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
    # Check for multiples of 3
    if (3 not in [x % 3 for x in lst]):
        # Check for multiples of 4
        if (4 not in [x % 4 for x in lst]):
            # Square all entries
            for i in range(len(lst)):
                lst[i] = lst[i] ** 2
        # Cube all odd numbers
        for i in range(len(lst) - 1):
            if (lst[i] % 2 == 1):
                lst[i] = lst[i] ** 3
    # Sum all entries
    return sum(lst)
