
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

    # Simple way
    # return sorted(lst)[1] if len(lst) > 1 else None

    # Best way
    # return min(lst[1:], key=lambda x: lst.index(x)) if len(lst) > 1 else None

    # Custom way
    # Set the first element of the list as the smallest and check the rest of the list
    # If there is a smaller element, then update the smallest element
    smallest = lst[0]
    second_smallest = None
    for number in lst[1:]:
        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif smallest < number < second_smallest or second_smallest is None:
            second_smallest = number
    return second_smallest
