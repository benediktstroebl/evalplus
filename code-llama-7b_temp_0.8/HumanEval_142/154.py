


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
    result = 0
    # Write your code here.
    # Use the index of the item in the list to determine if the item should be cubed, squared, or not affected.
    for index, item in enumerate(lst):
        if index % 3 == 0:
            result += item ** 3
        elif index % 4 == 0:
            result += item ** 4
        else:
            result += item
    return result


