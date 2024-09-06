
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
    else:
        # Find the maximum value in the list
        max_val = max(lst)

        # Find the minimum value that should be in the front of the list
        min_val = min(lst)

        # Find the remaining values in the list
        remaining_vals = [lst[i] for i in range(1, len(lst)) if lst[i] != max_val]

        # Sort the remaining values in a strange order
        strangely_sorted_remaining_vals = [max(remaining_vals)]
        for val in remaining_vals:
            if val > max_val:
                strangely_sorted_remaining_vals.append(val)
            else:
                strangely_sorted_remaining_vals.append(max(remaining_vals))

        # Reverse the order of the sorted values
        sorted_strangely_sorted_remaining_vals = [sorted(val)[::-1] for val in strangely_sorted_remaining_vals]

        # Return the list with the values in the strange order
        return sorted_strangely_sorted_remaining_vals[0] + sorted_strangely_sorted_remaining_vals[1:]
