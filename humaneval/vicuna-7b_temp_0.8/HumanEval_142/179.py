


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
    # Get all indices of the list
    indices = [i for i, el in enumerate(lst)]
    
    # Create an empty dictionary to store the squared and cubed values
    values_to_sum = {}
    
    for i, el in enumerate(indices):
        if (i % 3 == 0 and el % 3 == 0) or (i % 4 == 0 and el % 4 == 0):
            if el in values_to_sum:
                values_to_sum[el] += el**2
            else:
                values_to_sum[el] = el**2
        elif (i % 3 == 0 or i % 4 == 0) and el not in values_to_sum:
            values_to_sum[el] = el**3
    
    return sum(values_to_sum.values())
