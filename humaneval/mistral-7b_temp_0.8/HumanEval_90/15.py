
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
    #print(f"lst = {lst}")
    #print(f"len(lst) = {len(lst)}")
    #print(f"lst[1:] = {lst[1:]}")
    #print(f"len(lst[1:]) = {len(lst[1:])}")
    #print(f"lst[1:][1:] = {lst[1:][1:]}")
    #print(f"len(lst[1:][1:]) = {len(lst[1:][1:])}")

    #if (len(lst) > 2) and (len(lst[1:]) > 1):
    #    return min(lst[1:][1:])
    #return None
    if (len(lst) > 1) and (len(lst) < 4):
        return min(lst[1:])
    else:
        return min(lst[1:][1:])



