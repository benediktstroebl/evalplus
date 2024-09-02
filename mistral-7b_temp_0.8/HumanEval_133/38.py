

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
    # convert the list into ints
    int_lst = []
    for i in lst:
        int_lst.append(int(i))
    # make a sum_squares list
    sum_squares_lst = []
    # iterate through the list
    for i in range(len(int_lst)):
        # square the number
        square = int_lst[i] ** 2
        # round to the nearest upper integer
        round_up = round(square)
        # append the round up number to the sum_squares list
        sum_squares_lst.append(round_up)
    # add up the list of numbers
    sum_squares_add = sum(sum_squares_lst)
    return sum_squares_add

