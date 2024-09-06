
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
    # Define the target list
    target_list = []

    # Iterate through the input list
    for x in lst:
        # Find the index of the current number in the target list
        i = target_list.index(x)

        # If the current number is the first time it appears in the target list, add it to the beginning
        if i == -1:
            target_list.insert(0, x)
        # If the current number is the last number in the target list, add it to the end
        elif i == len(target_list) - 1:
            target_list.append(x)
        # If the current number is not the first or last time it appears in the target list, move all elements after it to the end
        else:
            target_list[i:].insert(0, x)

    return target_list