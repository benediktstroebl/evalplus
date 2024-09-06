def is_sorted(lst):
    # Count the unique elements and sort the list
    unique, sorted_list = set(lst), sorted(lst)
   
    # If unique elements are more than elements in the list,
    # Then it's not sorted
    if len(unique) > len(sorted_list):
        return False

    # Otherwise, check if sorted_list matches original lst
    for num in lst:
        if num not in unique:
            return False
    return True