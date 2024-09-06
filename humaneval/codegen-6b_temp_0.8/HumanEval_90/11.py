
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
    # Iterate thru the list
    # The first element is the 2nd smallest.
    
    # Keep a stack of tuples (v,i)
    
    # When popping an element, if the popped element is larger than what is in stack, return the last element in the stack
    # Else return the element
    
    # Time: O(n)
    # Space: O(n)
    
    stack = []
    
    for i, element in enumerate(lst):
        stack.append((element, i))
    
    while len(stack) > 1:
        smallest = min(stack)
        stack.remove(smallest)
        
        if stack[-1][0] < smallest[0]:
            return stack[-1][0]
    
    if len(stack) == 1:
        return stack[0][0]
    
    return None

assert(next_smallest([1, 2, 3, 4, 5]) == 2)
assert(next_smallest([5, 1, 4, 3, 2]) == 2)
assert(next_smallest([]) == None)
assert(next_smallest([1, 1]) == None)
assert(next_smallest([9, 3, 1, 7, 9]) == 3)
assert(next_smallest([3, 5, 4, 3, 1, 3, 7, 9]) == 3)
assert(next_smallest([9, 3, 1, 7, 9, 1]) == 1)
assert(next_smallest([39, 3, 1, 7, 9, 1]) == 1)
assert(next_smallest([1, 3, 4, 2, 16, 8]) == 4)
assert(next_smallest([1, 3, 4, 2, 16, 8, 13]) == 4)
assert(next_smallest([1, 3, 4, 2, 16, 8, 13, 9]) == 4)
assert(next_smallest([1, 3, 4, 2, 16, 8, 13, 9, 17]) == 4)
assert(next_smallest([1, 3, 4, 2, 16, 8, 13, 9, 17, 19]) == 4)
assert(next_small