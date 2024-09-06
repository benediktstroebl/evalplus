def strange_sort_list(lst):
    # Helper function to find the max element from the remaining list
    def max_from_remaining(L):
        max_so_far = float('-inf')
        for num in L:
            if num > max_so_far:
                max_so_far = num
        return max_so_far

    # Base case: If the list is empty, return it
    if not lst:
        return lst

    # Otherwise, return the minimum value followed by the max of the remaining list
    return strange_sort_list([min(lst), max_from_remaining(lst[1:])] + lst[2:])