
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
    # Solution 1 - Using while loop
    # lst.sort()
    # i = 0
    # while i < len(lst)-1:
    #     if lst[i] != lst[i+1]:
    #         return False
    #     i += 1
    # return True

    # Solution 2 - Using for loop
    # lst.sort()
    # for i in range(0,len(lst)-1):
    #     if lst[i] != lst[i+1]:
    #         return False
    # return True

    # Solution 3 - Using enumerate
    lst.sort()
    for i, num in enumerate(lst):
        if num != lst[i+1]:
            return False
    return True

