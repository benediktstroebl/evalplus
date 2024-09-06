


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
    # First, check if all the elements in the list are positive
    if all(lst[i].is_positive for i in range(len(lst))):
        # Initialize the sum to 0
        sum = 0
        # Loop through the list and calculate the sum of the squares
        for i in range(len(lst)):
            if (i % 3 == 0) and (i % 4 == 0):
                # If the current element is a square, increment the sum
                sum += lst[i] ** 2
            else:
                # If the current element is a cube, increment the sum
                sum += lst[i] ** 3
            # Check if we need to append the current element to the list
            if i != len(lst) - 1:
                lst.append(sum)
        return sum
    else:
        return 0