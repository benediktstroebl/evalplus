
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

    # 1. Find minimum of the list
    # 2. Append it to new list
    # 3. Remove it from the list
    # 4. Find maximum of the list
    # 5. Append it to new list
    # 6. Remove it from the list
    # 7. Repeat while list is not empty
    #
    # Runtime: O(n)
    # Condition: Only one minimum and one maximum

    result = []
    while lst:
        min_value = min(lst)
        max_value = max(lst)
        result.append(min_value)
        result.append(max_value)
        lst.remove(min_value)
        lst.remove(max_value)
    return result
