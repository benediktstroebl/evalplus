
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
    # step 1: initialize a counter variable
    counter = 0
    # step 2: traverse the list
    while counter < len(lst) - 1:
        # step 3: increment the counter
        counter += 1
        # step 4: check if the current element is less than the next
        if lst[counter - 1] > lst[counter]:
            # step 5: return false if they are not
            return False
    # step 6: return true if the counter is equal to the length of the list
    return True

