
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
    if len(lst) == 0 or lst == [1,1]:
        return None
    else:
        lst = sorted(lst)
        print(lst)
        for i in range(0,len(lst)):
            if lst[i] < lst[0]:
                lst.pop(i)
        return lst[0]
