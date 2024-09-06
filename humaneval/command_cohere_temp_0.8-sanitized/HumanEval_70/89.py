def strange_sort_list(lst):
    # Output list
    out = []

    # Helper function to recursively sort the list
    def strange_sort(li):
        # Base case: If the list is empty, return it
        if len(li) == 0:
            return li
        # Otherwise, grab the minimum value and sort the rest
        else:
            minval = min(li)
            rest = li[li != minval]
            rest_sorted = strange_sort(rest)
            return [minval] + rest_sorted

    # Apply strange sorting
    return strange_sort(lst)