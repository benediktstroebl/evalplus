


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
    # Check if the list has at least 3 elements
    if len(lst) < 3:
        return 0

    # Create a new list to store the results
    results = []

    # Iterate over the elements in the list
    for element in lst:
        # If the element is not a multiple of 3 or 4, it should be added to the results list
        if not ((element % 3) == 0 and (element % 4) == 0):
            results.append(element)

    # If the list has at least 3 elements, the results list will have at least 4 elements, which is a multiple of 3 and 4
    if len(results) >= 4:
        # For each element in the results list, square the element if its index is a multiple of 3, cube the element if its index is a 
        # multiple of 4, and add the element to the sum
        result = 0
        for element in results:
            if (element % 3) == 0:
                result += element ** 2
            elif (element % 4) == 0:
                result += element ** 3
            else:
                result += element
        return result
    return 0


