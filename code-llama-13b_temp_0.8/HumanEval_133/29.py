

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
    # Step 1: Ceil each element in the list
    ceil_lst = []
    for el in lst:
        ceil_lst.append(math.ceil(el))

    # Step 2: Square each element
    sqaure_lst = []
    for el in ceil_lst:
        sqaure_lst.append(el**2)

    # Step 3: Sum the squares
    return sum(sqaure_lst)
