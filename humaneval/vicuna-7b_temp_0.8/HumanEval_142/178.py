


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
    # check if the input list is empty
    if not lst:
        return 0
    # check if the input list is a single element
    if not len(lst):
        return 1
    # initialize the sum of squares to zero
    sum_squares = 0
    # loop through each element in the list
    for i, num in enumerate(lst):
        # check if the index of the current element is a multiple of 3 or 4
        if (i % 3 == 0 or i % 4 == 0):
            # square the number if the index is a multiple of 3, cube if the index is a multiple of 4
            num = (num * (i % 3 == 0)) if (i % 3 == 0) else (num * (i % 4 == 0)) if (i % 4 == 0) else num
        # add the number to the sum of squares
        sum_squares += num ** 2
    return sum_squares

