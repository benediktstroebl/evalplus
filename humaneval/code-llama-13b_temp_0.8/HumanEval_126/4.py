
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
    # lst = [1,2,2,3,3,4]
    # lst = [1,2,3,4,5,6,7,8]
    # lst = [2,1]
    # lst = [3,2,1]
    # lst = [1,2,2,3,3,4]
    # lst = [1,2,2,2,3,4]
    # lst = [1,2,3,4,5,6,7,8,9]
    # lst = [1,3,2,4,5,6,7,8,9]
    # lst = [1,3,4,2,5,6,7,8,9]
    # lst = [1,3,4,5,2,6,7,8,9]
    # lst = [1,3,4,5,6,2,7,8,9]
    # lst = [1,3,4,5,6,7,2,8,9]
    # lst = [1,3,4,5,6,7,8,2,9]
    # lst = [1,3,4,5,6,7,8,9,2]
    # lst = [1,3,4,5,6,7,8,9,2,2]
    # lst = [1,2,3,4,5,5,6,7,8,9]
    # lst = [1,2,3,4,5,5,5,6,7,8,9]
    # lst = [1,2,3,4,5,5,5,6,7,8,9,10]
    # lst = [10,9,8,7,6,5,4,3,2,1,0]
    # lst = [10,9,8,7,6,5,4,3,2,1]
    # lst = [0]
    # lst = [0,0]
    # lst = [1,1]
    # lst = [1,1,1]
    # lst = [1,2]
    # lst = [
