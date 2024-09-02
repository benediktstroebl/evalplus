
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
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    return min(lst[1:], key=lst[0].key())[0]

lst = sorted(my_list, key=lambda x: x.key)
for i in range(1, len(lst)):
    if next_smallest(lst[:i]) is not None:
        return next_smallest(lst[:i])
    if lst[i].key() < next_smallest(lst[:i]):
        return lst[i]
return None