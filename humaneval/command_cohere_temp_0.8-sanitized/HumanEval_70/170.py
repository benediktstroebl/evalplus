def strange_sort_list(lst):
    # Helper function to find the max element from the remaining list
    def max_from_remaining(L):
        max_so_far = float('-inf')
        for x in L:
            if x > max_so_far:
                max_so_far = x
        return max_so_far

    # Special case when empty list
    if not lst:
        return lst

    # Sorting the list
    return [x for i, x in enumerate(lst) if i == 0 or x == max_from_remaining(lst[:i-1])]