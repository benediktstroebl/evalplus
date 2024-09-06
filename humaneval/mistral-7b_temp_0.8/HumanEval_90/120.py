
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
    # lst.sort()
    # lst = lst[::-1]
    # print(lst)
    # if len(lst) == 1:
    #     return None
    # elif lst[0] == lst[1]:
    #     return None
    # else:
    #     return lst[0]

    # #1
    # if len(lst) == 1:
    #     return None
    # elif lst[0] == lst[1]:
    #     return None
    # else:
    #     return lst[0]
    # #2
    # if len(lst) < 2:
    #     return None
    # else:
    #     return sorted(lst)[1]
    # #3
    # if len(lst) < 2:
    #     return None
    # else:
    #     return min(lst[1:])

    # #4
    # if len(lst) == 0:
    #     return None
    # elif len(lst) == 1:
