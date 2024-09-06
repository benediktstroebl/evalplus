


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
    # Create an empty list to store the squared and cubed integers
    squared = []
    cubed = []
    
    # Iterate over the list
    for num in lst:
        # If the index is a multiple of 3, square the number
        if (num % 3 == 0):
            squared.append(num**2)
        # If the index is a multiple of 4, cube the number
        elif (num % 4 == 0):
            cubed.append(num**3)
        else:
            squared.append(num)
            cubed.append(num)
    
    # Add the squared and cubed numbers to the main list
    return sum(squared) + sum(cubed)
