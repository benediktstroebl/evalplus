

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

    #squaring all the elements of list
    lst_squared = [x**2 for x in lst]
    print(lst_squared)

    #Rounding the squared list to the upper int
    lst_rounded_to_int = [round(x, 0) for x in lst_squared]
    print(lst_rounded_to_int)

    #Adding the squared and rounded list
    print(sum(lst_rounded_to_int))




