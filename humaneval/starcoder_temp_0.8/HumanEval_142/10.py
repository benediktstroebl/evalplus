


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
    # Define a list to store the squared and cubed integers
    new_lst = []
    # Define a variable to keep track of the sum
    total_sum = 0
    # Loop through the list of integers
    for index, entry in enumerate(lst):
        # Condition to keep track of index of multiple of 3
        if index % 3 == 0:
            # Append the squared value of the integer to the list
            new_lst.append(entry ** 2)
        # Condition to keep track of index of multiple of 4 but not a multiple of 3
        elif index % 4 == 0:
            # Append the cubed value of the integer to the list
            new_lst.append(entry ** 3)
        # Condition to keep track of all other indexes
        else:
            # Append the integer to the list
            new_lst.append(entry)
    # Loop through the new list of integers
    for entry in new_lst:
        # Add the integer to the total sum
        total_sum += entry
    # Return the total sum
    return total_sum
