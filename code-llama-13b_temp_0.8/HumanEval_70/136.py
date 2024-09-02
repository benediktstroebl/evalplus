
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

    # point to the start of the list
    index = 0

    # while we haven't reached the end of the list
    while index < len(lst):
        # find the smallest value in the list
        smallest = lst[index]
        # find the index of the smallest value in the list
        smallest_index = index

        # find the largest value in the list after the minimum
        for i in range(index + 1, len(lst)):
            if lst[i] > smallest:
                smallest = lst[i]
                smallest_index = i

        # swap the smallest and maximum value
        lst[index], lst[smallest_index] = lst[smallest_index], lst[index]

        # increase the index
        index += 1

    return lst
