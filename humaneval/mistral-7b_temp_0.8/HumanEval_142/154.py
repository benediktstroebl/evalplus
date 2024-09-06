


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
    square_val = []
    cube_val = []
    # Checking the input to see if it is empty or not.
    if len(lst) == 0:
        return 0
    # Checking the length of the list for the indexes that are a multiple of 3 and 4.
    elif len(lst) % 3 == 0 and len(lst) % 4 == 0:
        for idx, value in enumerate(lst):
            if idx % 3 == 0:
                square_val.append(value ** 2)
            elif idx % 4 != 0:
                cube_val.append(value ** 3)
        return sum(square_val) + sum(cube_val)
    # Checking the length of the list for the indexes that are a multiple of 3 and not a multiple of 4.
    elif len(lst) % 3 == 0:
        for idx, value in enumerate(lst):
            if idx % 3 == 0:
                square_val.append(value ** 2)
