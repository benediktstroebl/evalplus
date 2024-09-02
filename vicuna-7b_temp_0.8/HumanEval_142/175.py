


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
    # check if any index is a multiple of 3
    if any(i % 3 == 0 for i in range(len(lst))):
        # check if any index is a multiple of 4
        if any(i % 4 == 0 for i in range(len(lst))):
            # check if all entries are positive
            if any(lst[i] < 0 for i in range(len(lst))):
                return -1
            # square all even index entries
            squared_lst = [j ** 2 if j % 2 == 0 else j for j in lst]
            # cube all odd index entries
            cubed_lst = [j ** 3 if j % 3 == 1 else j ** 2 if j % 2 == 0 else j for j in squared_lst]
            return sum(cubed_lst)
        else:
            return -1
    else:
        return 0

