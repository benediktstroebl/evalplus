


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
    # Step 1: Let sum be initialized as 0.
    sum = 0
    # Step 2: For each integer entry in the list, index is the index of that entry.
    for index in range(len(lst)):
        # Step 3: If index is a multiple of 3, set the entry to its square.
        if index % 3 == 0:
            lst[index] *= lst[index]
        # Step 4: Else if index is a multiple of 4, set the entry to its cube.
        elif index % 4 == 0:
            lst[index] **= 3
        # Step 5: Increment sum by the entry.
        sum += lst[index]
    # Step 6: Return sum.
    return sum

