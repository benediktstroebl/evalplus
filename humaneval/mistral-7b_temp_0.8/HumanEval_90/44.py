
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    #next smallest:
    # if there are 2 numbers in the list return the bigger one
    # else if there is only one number return none
    # else, if there are 2 or more numbers, return the second smallest number.
    #


    if len(lst) == 1:
        return None

    elif len(lst) == 2:
        if lst[0] < lst[1]:
            return lst[0]
        else:
            return lst[1]

    else:
        smallest = lst[0]
        second_smallest = None

        for i in range(1, len(lst)):
            if lst[i] < smallest:
                second_smallest = smallest
                smallest = lst[i]
            elif lst[i] > smallest and lst[i] < second_smallest:
                second_smallest = lst[i]

        return second_smallest
