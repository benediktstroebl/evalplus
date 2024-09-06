
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
    n = len(lst)
    if n==1:
        return None
    a = [1]*n
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]>lst[j]:
                a[i] = lst[j]
    return a[0]
