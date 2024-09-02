

def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    # TODO: Write a solution!
    # increment all elements
    # iterate through each element in l
    # check if i is equal to the last element in l
    # increment element
    # add element to new_list
    # return new_list
    new_list = []
    for i in range(len(l)):
        if i == len(l)-1:
            new_list.append(l[i]+1)
        else:
            new_list.append(l[i]+1)
    return new_list

