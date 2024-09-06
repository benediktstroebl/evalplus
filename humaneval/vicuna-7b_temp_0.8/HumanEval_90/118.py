
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
    i = 0
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
        elif num == smallest:
            i += 1
    return smallest if i == 0 else None

lst = [6, 4, 9, 3, 2, 1]
lst = list(map(int, input().split()))
smallest = next_smallest(lst)
