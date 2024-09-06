
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

    # Sorting a list is O(nlogn) time complexity
    # if sorted_lst == sorted(lst):
    #     return True
    # return False

    # O(n) time complexity
    sorted_lst = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                sorted_lst.append(lst[i])
            else:
                sorted_lst.append(lst[j])
            if sorted_lst != sorted(lst):
                return False
    return True
