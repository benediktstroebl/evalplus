
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    list = lst
    largest = None
    smallest = None
    # Create a tuple that holds the largest integer of negative and the smallest integer of positive
    # If the list is empty return None
    # If the list has no negative integer return None
    # If the list has no positive integer return None
    if len(list) == 0:
        return largest, smallest
    elif len(list) > 0 and min(list) < 0:
        return max(list), min(list)
    else:
        return largest, smallest

    # Use a loop to go through each index of the list
    # If the index is a positive integer and is smaller than the smallest, return smallest and the index
    # If the index is a negative integer and is greater than the largest, return largest and the index
    # If the index is a positive integer and is greater than the smallest, return the index
    # If the index is a negative integer and is smaller than the largest, return the index
