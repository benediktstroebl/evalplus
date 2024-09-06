
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
    # Step 1: Find the minimum value
    min_val = min(lst)

    # Step 2: Find the maximum value of remaining values
    max_remainder = max(lst[1:])

    # Step 3: Append the minimum value to the list
    lst.append(min_val)

    # Step 4: Append the maximum value of remaining values to the list
    lst.append(max_remainder)

    # Step 5: Repeat step 3 and 4 for all the remaining values
    for i in range(1, len(lst)):
        min_val = min(lst[i:])
        max_remainder = max(lst[i:])
        lst.append(min_val)
        lst.append(max_remainder)

    return lst
