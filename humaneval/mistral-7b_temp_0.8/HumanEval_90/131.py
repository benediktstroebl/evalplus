
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
    if len(lst)==0:
        return None
    elif len(lst)==1:
        return None
    else:
        for i in range(1,len(lst)):
            if lst[i]<lst[i-1]:
                return lst[i]

        return lst[i-1]

    # find the second smallest number in a list
    # if there are less than 2 numbers in the list, return None
    # if there are 2 numbers in the list, return the second number
    # if there are more than 2 numbers in the list, loop through the list and find the second smallest number
    # return the second smallest number
