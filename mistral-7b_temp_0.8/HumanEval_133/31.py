

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
    """
    Ceiling Function
    It returns the smallest integer value that is equal to or greater than the given number.
    
    """
    # ceil(4.75) = 5
    # ceil(3) = 3
    # ceil(1.9) = 2
    # ceil(0) = 0
    # ceil(-3.2) = -3
    # ceil(-3) = -3

    # A list comprehension is a Python syntax that lets you build lists by evaluating an expression for each item in a given list.
    # [expressions for item in iterables]
    # lst = [item for item in iterables]
    # [item * 2 for item in [1, 2, 3, 4, 5]] # [2, 4, 6, 8, 10]
    # [item + 2 for item in [1, 2, 3, 4, 5]] # [3, 4, 5, 6, 7]
    # [i + 2 for i in
