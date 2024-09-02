


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
    
    # Empty list
    if len(lst) == 0:
        return 0
    # Create a list of index of the list
    list_index = [index for index in range(len(lst))]
    # Create a list of index that is multiple of 3
    multiple_3 = [multiple for multiple in list_index if multiple % 3 == 0]
    # Create a list of index that is multiple of 4
    multiple_4 = [multiple for multiple in list_index if multiple % 4 == 0]
    # Create a list of index that is not multiple of 3 or 4
    no_multiple_3_or_4 = [multiple for multiple in list_index if multiple not in multiple_3 and multiple not in multiple_4]
    
    # Calculate the sum of squarred entries for entries that are multiple of 3
    lst_multiple_3 = [entry**2 for multiple,entry in enumerate(lst) if multiple in multiple_3]
    # Calculate the sum of cubed entries for entries that are multiple of 4
    lst_multiple_4 = [entry**3 for multiple,entry in enumerate(lst) if multiple in multiple_4]
    # Calculate the sum of entries for entries that are not multiple of 3 or 4
    lst_no_multiple_3_or_4 = [entry for multiple,entry in enumerate(lst) if multiple in no_multiple_3_or_4]
    
    # Combine the lists
    lst_new = lst_no_multiple_3_or_4 + lst_multiple_3 + lst_multiple_4
    # Calculate the sum of the list
    lst_sum = sum(lst_new)
    return lst_sum
    
    
