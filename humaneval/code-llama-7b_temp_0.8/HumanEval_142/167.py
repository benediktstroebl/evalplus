


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
    
    # Using a list comprehension, square the index if its multiple of 3, and cube it if its multiple of 4.
    lst_3 = [i**2 if (n % 3 == 0) else i for n, i in enumerate(lst)]
    
    # Use a list comprehension to multiply all elements of the list by themselves.
    lst_4 = [i**3 if (n % 4 == 0) else i for n, i in enumerate(lst)]
    
    # Use a list comprehension to sum up all elements in the list.
    lst_34 = [i**3 if (n % 4 == 0) and (n % 3 == 0) else i for n, i in enumerate(lst)]
    
    # Return the sum of all elements in the list.
    return sum(lst_3 + lst_4 + lst_34)














