
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
    # Convert list to string
    lst = str(lst)
    # Split string into list of individual characters
    lst = lst.split(" ")
    # Sort string into ascending order
    lst = sorted(lst)
    # Convert string back to list
    lst = list(lst)
    # Check if the list has more than 1 duplicate of the same number
    if lst.count(lst[0]) > 1:
        return False
    # Check if the list is sorted
    if lst == lst[::-1]:
        return True
    else:
        return False
