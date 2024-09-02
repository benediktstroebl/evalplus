
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    # EXPLANATION OF SOLUTION:
    # I know that I should use the built-in functions for minimum and maximum
    # and how to cycle through a list. But I had no idea how to implement it.
    # Then I found this explanation:
    # https://www.quora.com/What-is-the-best-way-to-do-strange-sorting-in-Python

    return sorted(lst, key=lambda x: sum(sorted(lst)[::2*lst.index(x)-1]))

