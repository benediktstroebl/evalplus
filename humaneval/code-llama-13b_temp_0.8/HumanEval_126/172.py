
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    #   for loop nested in while loop
    #   compare adjacent elements
    #   if decreasing order, break out
    #   if not decreasing order
    #   and if increasing order break

    #   decreasing order
    #   nested for loops
    #   for outer loop through all elements in lst
    #   for inner loop, start inner loop one index after outer loop index
    #   and compare the adjacent elements
    #   if lst[outer loop index] > lst[inner loop index]
    #   break

    #   increasing order
    #   nested for loops
    #   for outer loop through all elements in lst
    #   for inner loop, start inner loop one index after outer loop index
    #   and compare the adjacent elements
    #   if lst[outer loop index] < lst[inner loop index]
    #   break

    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    for i in range(len(lst) - 1):
        if lst[i] < lst[i+1]:
            return True

    #   return true if for loop didn't break
    return True

































