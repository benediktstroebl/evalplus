
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

    # Check if list is empty
    if lst == []:
        return (None, None)

    # Check if the list contains only 0
    if lst.count(0) == len(lst):
        return (None, None)

    # Check if the list contains only negative or positive integers
    if lst.count(0) == 0:
        largest = -100
        smallest = 100

        # Check if integers are negative
        for i in range(len(lst)):
            if lst[i] < 0 and lst[i] > largest:
                largest = lst[i]

        # Check if integers are positive
        for i in range(len(lst)):
            if lst[i] > 0 and lst[i] < smallest:
                smallest = lst[i]

        return (largest, smallest)

