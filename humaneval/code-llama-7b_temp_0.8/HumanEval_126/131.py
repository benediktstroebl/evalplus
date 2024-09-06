
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
    # Step 0: Check base cases
    if len(lst) <= 1:
        return True

    # Step 1: Get initial sorted list
    sorted_list = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] > sorted_list[-1]:
            sorted_list.append(lst[i])
        else:
            return False

    # Step 2: Check duplicates
    for i in range(1, len(lst)):
        if lst[i] in sorted_list:
            return False

    return True
