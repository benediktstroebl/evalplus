
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
    if not lst:
        return []

    # sort the list in descending order
    lst = sorted(lst, reverse=True)

    # find the first and last element
    first = lst[0]
    last = lst[-1]

    # find the middle element
    middle = lst[1]

    # use the first and last element to find the second element
    second = lst[0]

    # continue the process until the end of the list
    for i in range(2, len(lst)):
        # find the middle element
        middle = lst[i]

        # use the previous and next elements to find the next element
        next = lst[i - 1]

        # use the first and middle elements to find the previous element
        prev = lst[i]

        # append the elements in the correct order
        lst = [first, middle, last, second, next, prev]

    return lst
