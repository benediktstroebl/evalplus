
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
    if lst == []:
        return (None, None)
    else:
        negative_integers = []
        positive_integers = []
        for i in range(len(lst)):
            if lst[i] < 0:
                negative_integers.append(lst[i])
            elif lst[i] > 0:
                positive_integers.append(lst[i])

        if negative_integers == []:
            return None, positive_integers[0]
        elif positive_integers == []:
            return negative_integers[0], None
        else:
            return max(negative_integers), min(positive_integers)


