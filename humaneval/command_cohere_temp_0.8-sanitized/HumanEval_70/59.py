def strange_sort_list(lst):
    # Helper function to find the max element from the remaining list
    def max_remaining(L):
        max_so_far = float('-inf')
        for x in L:
            if x > max_so_far:
                max_so_far = x
        return max_so_far
    
    # Base case: if the list is empty or contains only one element
    if len(lst) < 2:
        return lst
    
    # Start with the minimum value (first element)
    min_value = lst[0]
    # Sort the remaining list using the strange sorting algorithm
    sorted_list = [min_value]
    lst.remove(min_value)
    while len(lst) > 0:
        # Find the maximum of the remaining elements
        max_value = max_remaining(lst)
        # Add the maximum element to the sorted list
        sorted_list.append(max_value)
        # Remove the maximum element from the remaining list
        lst.remove(max_value)
    # Return the sorted list
    return sorted_list