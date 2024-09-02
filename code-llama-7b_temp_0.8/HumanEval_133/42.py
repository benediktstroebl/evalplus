

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


    # =============================================================================
    #     # This is a way to get the square of a number
    #     square_of_num = (num)**2
    #     # This is a way to round up
    #     ceil_of_num = math.ceil(num)
    #     return square_of_num * ceil_of_num
    # =============================================================================


    # =============================================================================
    #     # The above works but it is not pythonic
    #     # We can do better
    #     # We can use the round up formula 
    #     # This is the formula
    #     #   = (A + 1) - 0.5
    #     # Where A is the original number
    #     # So for the above 
    #     #   = (A + 1) - 0.5
    #     #   = (1 + 1) - 0.5
    #     #   = 3 - 0.5
    #     #   = 2.5 - 0.5
    #     #   = 2 - 0.5
    #     #   = 1.5
    #     #   = 2
    #     #   = 2
    #     # So you need to use that formula
    #     # I know that the math library has a function that does this
    #     # But here is how you do it without a library
    #     # Now we can do the same for the square of the number
    #     # Just remember to square it first
    #     #   = (num * num) * ceil
    #     #   = (A * A) * (A + 1) - 0.5
    #     #   = (A * A) * (1 + 1) - 0.5
    #     #   = (A * A) * 2 - 0.5
    #     #   = (A * A) * 2 - 0.5
    #     #   = (A * A) * 2 - 0.5
    #     #   = (A * A) * 
