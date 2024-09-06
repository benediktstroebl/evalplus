

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
    # round each element in the list to the upper int(Ceiling)
    rounded_lst = []
    for x in lst:
        rounded_lst.append(int(math.ceil(x)))
    # print(rounded_lst)

    # Step 2:
    # squaring each element in the list and summing them
    squared_lst = []
    for x in rounded_lst:
        squared_lst.append(x * x)
    return sum(squared_lst)
    
