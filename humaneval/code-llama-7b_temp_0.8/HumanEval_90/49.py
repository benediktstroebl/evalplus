
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
    # Your code here
    # if len(lst) == 2:
    #     if lst[0] < lst[1]:
    #         return lst[0]
    #     elif lst[0] > lst[1]:
    #         return lst[1]
    #     else:
    #         return None
    # else:
    #     if lst[0] < lst[1]:
    #         return lst[0]
    #     else:
    #         return next_smallest(lst[1:])

    next_list = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[j] < lst[i]:
                next_list.append(lst[j])
            if lst[j] == lst[i]:
                continue
    if len(next_list) != 0:
        return next_list[0]
    else:
        return None
