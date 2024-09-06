
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
    negative = []
    positive = []
    #range(len(lst)) returns an iterator from 0 to length of list
    for i in range(len(lst)):
        #first if statement checks if i is less than 0
        if i < 0 and lst[i] > len(lst) and lst[i] < 0:
            negative.append(lst[i])
        #second if statement checks if i is greater than 0
        elif i > 0 and lst[i] > len(lst) and lst[i] > 0:
            positive.append(lst[i])
    if negative == []:
        return (None, None)
    elif positive == []:
        return (None, None)
    else:
        negative.sort(reverse=True)
        positive.sort()
        return (negative[0], positive[0])
