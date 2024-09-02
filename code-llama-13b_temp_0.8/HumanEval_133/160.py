

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    # Step 1:
    # initialize a variable and set it to 0
    # Step 2:
    # Iterate through the list
    # Step 3:
    # for each element in the list, round it to the upper int(Ceiling) first, and square it
    # add it to the variable in step 1
    # Step 4:
    # return the variable from step 1

    result = 0

    for element in lst:
        result += (int(math.ceil(element))**2)

    return result
