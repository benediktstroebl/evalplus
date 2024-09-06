
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
    # In real life, you'd have to sort the list first, which is the obvious way to do that.
    # But in this case, it's probably better to build it on paper.
    # For the first element, your list is empty, so there's nothing to compare to.
    # For the second element, your list contains only one element, so you can return that directly.
    # For the rest, you're going to loop through comparing element[index] to element[index + 1],
    # and return the smallest element of the remaining list.
    return min(lst[1:]) if lst[0] > lst[1] else None
