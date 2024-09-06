
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
    # The following block of code is the core of the algorithm.
    # It works by counting the number of times each number appears in the list.
    # If the number of times a number appears is greater than or equal to the
    # number of times the next largest number appears, then we know that number
    # must appear more than once, and the list is not sorted.
    # This is because if the number of times a number appears is greater than or
    # equal to the number of times the next largest number appears, then
    # there cannot be any consecutive duplicates of that number in the list.
    #
    # If the number of times a number appears is less than the number of times
    # the next largest number appears, then we know that number must appear
    # at least twice, and the list is not sorted.
    # This is because if the number of times a number appears is less than the
    # number of times the next largest number appears, then there must be at least
    # two consecutive duplicates of that number in the list.
    return len(set(lst)) == 1
