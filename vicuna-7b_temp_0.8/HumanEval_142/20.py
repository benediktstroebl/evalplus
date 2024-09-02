


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
    # Step 1: create a new list that will store the squared/cubed entries
    squared_cubed = []
    # Step 2: iterate through the input list and check if the index is a multiple of 3 or 4
    for i, val in enumerate(lst):
        if i % 3 == 0:
            squared_cubed.append(val**2)
        elif i % 4 == 0:
            squared_cubed.append(val**3)
        else:
            squared_cubed.append(val)
    # Step 3: add the non-squared/cubed entries to the result
    result = sum(lst)
    return result + sum(squared_cubed)

