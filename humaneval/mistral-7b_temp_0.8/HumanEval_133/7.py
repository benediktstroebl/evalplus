

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
    # I changed the input to a list of float values
    # I then ran a for loop that converted each element to an int
    # and stored it in a variable called squared_list
    # I then ran a for loop that converted each element to a string
    # and stored it in a variable called int_list
    # I then ran a for loop that converted each element to a float
    # and stored it in a variable called float_list
    # I then ran a for loop that added the squared_list to the
    # int_list to get the sum of squares
    # I then converted the float_list to an int and added it to the sum
    # I then converted the sum to a string and returned it
    squared_list = [int(i) for i in lst]
    int_list = [str(i) for i in squared_list]
    float_list = [float(i) for i in int_list]
    sum = sum(squared_list)
    sum = int(float_list[0] + sum)
    return sum

