
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
    # helper function
    def find_largest_smallest(lst, positive, negative):
        if positive == []:
            return (None, None)
        if negative == []:
            return (None, max(lst))
        if negative[0] < positive[0]:
            return (negative, max(lst))
        return (positive, min(lst))

    positive_numbers = []
    negative_numbers = []
    for num in lst:
        if num < 0:
            negative_numbers.append(num)
        else:
            positive_numbers.append(num)
    return find_largest_smallest(positive_numbers, negative_numbers, [])

