


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
    # Initializing Sum
    sum_of_squares = 0

    # Iterate over list elements
    for i in range(len(lst)):
        # If element is multiple of 3 then square the element and add to sum. Else if element is multiple of 4 then cube the element and add to sum. Else, just add the element to sum.
        if i % 3 == 0:
            sum_of_squares = sum_of_squares + (lst[i] * lst[i])
        elif i % 4 == 0:
            sum_of_squares = sum_of_squares + (lst[i] * lst[i] * lst[i])
        else:
            sum_of_squares = sum_of_squares + lst[i]

    return sum_of_squares
