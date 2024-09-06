


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
    # Check if the list is empty or not
    if not lst:
        return 0
    else:
        total = 0
        # Iterate through the list
        for num in lst:
            # If the index is a multiple of 3 or 4, square or cube the integer, else leave it as is
            if (num % 3 == 0) or (num % 4 == 0):
                num = num ** 2 if num % 3 == 0 else num ** 3 if num % 4 == 0 else num
            # Add the squared or cubed number to the total
            total += num
        return total

