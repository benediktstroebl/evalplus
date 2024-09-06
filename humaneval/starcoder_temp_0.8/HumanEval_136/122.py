
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
    # Your code here
    new_lst = []
    for num in lst:
        if num >= 0:
            new_lst.append(num)
    if len(new_lst) > 0:
        largest = max(new_lst)
        smallest = min(new_lst)
    else:
        largest = None
        smallest = None
    return (largest, smallest)
