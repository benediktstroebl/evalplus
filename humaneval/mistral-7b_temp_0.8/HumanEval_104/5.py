
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # Write your code here
    # You can use other python built-in functions
    # You can also write your own helper functions
    # You can't use list comprehension
    # You can't use for loops
    # You can't use while loops
    # You can't use return
    # You can't use conditional statements (if/elif/else)
    # You can't use for loops
    # You can't use while loops
    # You can't use return

    # *******  DO NOT CHANGE THE CODE BELOW  *******
    #
    # IMPORTANT: Write your code in the function above
    # Do not modify the code below
    # *******  DO NOT CHANGE THE CODE ABOVE  *******
    if x == []:
        return []

    return list(unique_digits(x[:-1]) + [x[-1]] if unique_digits(x[:-1]) + [x[-1]] else [])

