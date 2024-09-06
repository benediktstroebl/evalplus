


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
    # check if the input is a list
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    # create a new list to store the squares and cubes
    squares_and_cubes = []
    # iterate over each element in the input list
    for i, entry in enumerate(lst):
        if i % 3 == 0:
            squares_and_cubes.append(i**2)
        elif i % 4 == 0:
            squares_and_cubes.append(i**3)
        else:
            squares_and_cubes.append(entry)
    # sum up the elements in the new list
    return sum(squares_and_cubes)