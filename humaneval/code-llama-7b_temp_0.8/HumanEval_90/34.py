
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
    if len(lst) < 2:
        return None
    elif len(lst) == 2:
        return None
    else:
        list1 = lst[0]
        list2 = lst[1]
        for i in lst:
            if list1 > i and i < list2:
                list1 = i
            elif list1 < i and i < list2:
                list2 = i
        if list2 > list1:
            return list1
        else:
            return None
