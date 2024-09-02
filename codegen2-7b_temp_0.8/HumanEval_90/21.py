
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
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i!= j:
                if lst[j] > lst[i]:
                    print(lst[j],lst[i])
                    return lst[i]
    print(lst)
    

