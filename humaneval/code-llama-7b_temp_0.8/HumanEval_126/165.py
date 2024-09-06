
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
    #set of each unique value
    unique_values = set(lst)
    #set of all values in original list
    all_values = set(lst)
    #check if the length of sets are the same
    if len(unique_values) != len(all_values):
        return False

    #if the list is empty, return True
    if len(lst) == 0:
        return True

    #start at index 0
    current_index = 0

    #check the rest of the list for sorted order
    while current_index < len(lst) - 1:
        #if the next value is less than the current value, return False
        if lst[current_index] > lst[current_index+1]:
            return False
        #otherwise increment the index
        current_index += 1

    #if the list is sorted, return True
    return True
