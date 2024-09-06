


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

    if not isinstance(lst, list):
        raise TypeError('Input should be a list.')

    lst_length = len(lst)
    sum_of_squares = 0

    for index, entry in enumerate(lst):

        if (index+1) % 3 == 0:
            sum_of_squares += entry**2

        elif (index+1) % 4 == 0:
            sum_of_squares += entry**3

        elif (index+1) % 1 == 0:
            sum_of_squares += entry

        else:
            pass

    return sum_of_squares

