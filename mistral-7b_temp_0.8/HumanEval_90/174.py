
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
    # This is the first solution I found.
    # It uses the smallest set of lines.
    # It is probably the fastest solution.
    # But it is also the most confusing.
    # My first version of this function used a
    # list comprehension, but it was hard to read.
    # In my final version, I used two lists and
    # three for-loops.

    # This is the first solution I found.
    # It uses the smallest set of lines.
    # It is probably the fastest solution.
    # But it is also the most confusing.
    # My first version of this function used a
    # list comprehension, but it was hard to read.
    # In my final version, I used two lists and
    # three for-loops.
    #
    # 1. Create an empty list to store the smallest elements of the list.
    # 2. Create an empty list to store the elements of the list that are not in the smallest list.
    # 3. For each element in the list, check if it is in the smallest list. If it is, remove it from
