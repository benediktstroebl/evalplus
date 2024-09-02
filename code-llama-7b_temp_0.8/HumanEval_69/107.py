
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # Set the output to the first number in the list
    output = lst[0]
    
    # For each number in the list, if it is larger than the current output and greater than 0, update it
    for i in range(len(lst)):
        if lst[i] > output and lst[i] > 0:
            output = lst[i]
    
    # Set a count variable to 0
    count = 0
    
    # For each number in the list, if it matches the output and greater than 0, add 1 to count
    for i in range(len(lst)):
        if lst[i] == output and lst[i] > 0:
            count += 1
            
    # If count is less than or equal to the number at the output index, set the output to -1
    if count <= lst[output-1]:
        output = -1
    
    # Return the output
    return output
    
