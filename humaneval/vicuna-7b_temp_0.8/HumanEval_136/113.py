
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
    if not lst:
        return None, None

    smallest = float('-inf')
    largest = float('inf')
    for num in lst:
        if num >= 0:
            smallest = min(smallest, num)
        else:
            largest = max(largest, num)

    return smallest, largest

lst = [2, 4, 1, 3, 5, 7, 0]
print(largest_smallest_integers(lst))
