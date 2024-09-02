
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
    # Use a helper variable to check the current number
    current = lst[0]
    # Keep track of the last number that was in the list
    last = lst[-1]
    # Iterate over the list
    for i in range(1, len(lst)):
        # Check if the current number is less than the last number
        if lst[i] < last:
            # Return False if there is more than one duplicate
            if (lst[i] == current) and (lst.count(current) > 1):
                return False
            # Otherwise, update the current number and last number
            current = lst[i]
            last = lst[-1]
        # Check if the current number is greater than the last number
        elif lst[i] > last:
            # If the current number is greater than the last number,
            # return True regardless of whether or not there are duplicates
            return True
        # If the current number is less than or equal to the last number,
        # increment the last number and check if there are more duplicates
        last += 1
    # If we've reached the end of the list and there is only one number,
    # return True
    return True