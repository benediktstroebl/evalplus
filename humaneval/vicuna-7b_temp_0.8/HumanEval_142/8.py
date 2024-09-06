


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
    # Find all multiples of 3 and 4 in the list
    multiples = [i for i in range(len(lst)) if (i % 3 == 0 or i % 4 == 0)]
    # Create a new list with only the multiples
    sq_multiples = [lst[i] ** (i % 3 == 0) if (i % 3 == 0) else lst[i] ** (i % 4 == 0) if (i % 4 == 0) else lst[i] for i in multiples]
    # Add 1 to each element so that we get the index of the element
    sq_multiples = [i + 1 for i in sq_multiples]
    # Calculate the sum of all elements in the new list
    sum = sum(sq_multiples)
    return sum
