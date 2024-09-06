import numpy as np
def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    # Convert the list to an array for easier manipulation
    arr = np.array(lst, copy=True)
    
    # Check if the input list is empty, return 0 if it is
    if arr.size == 0:
        return 0
    
    # Convert integers to floats to avoid integer overflow during square operation
    arr = arr.astype(float)
    
    # Square the numbers and convert to numpy array
    odd_numbers = np.where(arr % 2 == 1, arr ** 2, 0)
    odd_numbers = np.array(odd_numbers)
    
    # Sum the squared odd numbers
    result = np.sum(odd_numbers)
    
    return result