

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
    # round up each number
    # ------------------------------------------
    # We can use built in function ceil(x)
    # which returns the ceiling of x as a float,
    # the smallest integer value greater than or equal to x.

    # lst_ceiled = [ceil(item) for item in lst]

    lst_ceiled = [int(item) + 1 if item - int(item) >= 0.5 else int(item) for item in lst]
    print('lst_ceiled', lst_ceiled)

    # Step 2:
    # Compute sum of squared numbers
    # ------------------------------------------
    # lst_squared = [item * item for item in lst_ceiled]
    lst_squared = [item ** 2 for item in lst_ceiled]
    print('lst_squared', lst_squared)

    # Step 3:
    # Compute sum of the lst_squared
    # ------------------------------------------
    lst_squared_sum = sum(lst_squared)

    return lst_squared_sum

