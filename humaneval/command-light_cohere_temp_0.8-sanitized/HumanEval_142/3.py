def sum_squares(lst):
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries.

    Parameters:
    lst (list of integers)
    Returns:
    sum of all entries in the list
    """
    sum = 0
    for num in lst:
        if num%3 == 0 and num not in [0,1,2]:
            sum += num**2
        elif num%4 == 0 and num not in [0,1,2,3]:
            sum += num
    return sum