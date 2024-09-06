


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
    # Create a list of the indices of the elements in the list
    indices = [i for i, x in enumerate(lst)]
    # Create a list of tuples where the first element is the index and the second element is the value
    values = [(indices[i], x) for i, x in enumerate(lst)]
    # Create a new list to store the squared values if the index is a multiple of 3 or cubed values if the index is a multiple of 4
    result = []
    for i, x in enumerate(values):
        if i % 3 == 0:
            result.append((x[0]**2, x[1]))
        elif i % 4 == 0:
            result.append((x[0]**3, x[1]))
        else:
            result.append(x[1])
    # Return the sum of all the values in the new list
    return sum(result)

