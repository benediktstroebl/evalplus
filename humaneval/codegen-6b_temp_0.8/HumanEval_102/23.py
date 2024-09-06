
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    # Assign the upper and lower bounds
    upper_bound = x
    lower_bound = y

    # Upper and lower bounds should be at least 4.
    if upper_bound < 4:
        upper_bound = 4
    if lower_bound < 4:
        lower_bound = 4
    
    # Initialize the solution
    solution = -1
    
    # Keep checking until the solution is found by 
    # comparing the solution to each even number in range
    while solution == -1:
        # Check if the solution is in the range 
        if ((lower_bound % 2) == 0) and ((upper_bound % 2) == 0):
            # If the solution is in the range, return it
            solution = lower_bound
            break
        # If the solution is not in the range, check if the solution is
        # double of a number
        elif ((lower_bound % 2) != 0) or ((upper_bound % 2) != 0):
            # If the solution is not a double, move on to the next number
            lower_bound += 1
        # If the solution is double, decrease the upper_bound by 1
        else:
            upper_bound -= 1
    
    # Return the solution
    return solution
