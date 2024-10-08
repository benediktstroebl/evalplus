


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
    # Count the number of entries that are a multiple of 3 and 4
    count = 0
    for i in range(len(lst)):
        if (i % 3 == 0) or (i % 4 == 0):
            count += 1
    
    # If the number of entries is odd, set the count to 1
    if count % 2 != 0:
        count += 1
    
    # Calculate the sum of all entries
    sum = 0
    for i in range(len(lst)):
        if (i % 3 == 0) or (i % 4 == 0):
            sum += lst[i] ** 2
        else:
            sum += lst[i] ** 3
    
    # If the number of entries is odd, add a value to the sum
    if count % 2 != 0:
        sum += lst[-1] ** 2
    
    return sum
