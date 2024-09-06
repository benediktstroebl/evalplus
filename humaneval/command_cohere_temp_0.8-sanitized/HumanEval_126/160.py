def is_sorted(lst):
    # Count the unique elements and sort the list
    unique, sorted_list = set(lst), sorted(lst)
   
    # If unique elements are more than one and the list is not sorted, return False
    if len(unique) > 1 and sorted_list != lst:
        return False
    # Return True if the list is sorted or has only 1 unique element
    return True