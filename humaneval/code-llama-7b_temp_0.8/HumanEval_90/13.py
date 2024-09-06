
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

    # My solution

    smallest = min(lst)
    lst = lst[1:]
    new_lst = []
    for num in lst:
        if num != smallest:
            new_lst.append(num)
    if len(new_lst) == 0:
        return None
    else:
        return min(new_lst)

    # An elegant solution

    # if len(lst) < 2:
    #     return None
    # return sorted(lst)[1]

    # 1st solution

    # lst = list(enumerate(lst))
    # lst.sort(key=lambda x: x[1])
    # for i in range(len(lst) - 1):
    #     if lst[i][1] < lst[i+1][1]:
    #         return lst[i][1]
    # return None

