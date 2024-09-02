


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
    
    #ensure that lst is a list
    if not isinstance(lst, list):
        raise TypeError('lst must be a list')

    #if the list is empty, return 0
    if lst == []:
        return 0

    #if the list is not empty, continue
    else:
        #sum of squares
        sos = sum(lst[i]**2 for i in range(len(lst)) if i % 3 == 0)
        #sum of cubes
        soc = sum(lst[i]**3 for i in range(len(lst)) if i % 4 == 0)

        #return the sum of squares and cubes
        return sos + soc


