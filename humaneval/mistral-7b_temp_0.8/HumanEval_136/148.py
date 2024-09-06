
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


    if len(lst) == 0 or lst[0] > 0:
        return None, None

    #the value of min is the lowest value in the list
    min = lst[0]
    #the value of max is the lowest value in the list
    max = lst[0]

    #the value of num is the lowest value in the list
    #go through the list, and find the lowest number
    for num in lst:
        if num < min:
            min = num
        if num > max:
            max = num

    return max, min
