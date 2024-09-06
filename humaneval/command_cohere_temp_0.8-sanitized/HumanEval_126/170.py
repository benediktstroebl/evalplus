def is_sorted(lst):
    # Count the unique elements and sort the list
    unique_count = len(set(lst))
    sorted_lst = sorted(lst)
    
    # If unique elements are greater than or equal to 2 and the list is sorted, return True
    if unique_count >= 2 and sorted_lst == lst:
        return True
    # Otherwise, return False
    else:
        return False