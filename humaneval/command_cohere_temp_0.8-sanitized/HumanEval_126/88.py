def is_sorted(lst):
    # Count the unique elements and sort the list if it contains multiple unique elements
    if len(set(lst)) > 1 and lst != sorted(lst):
        return False
    # Check if there are duplicates and more than 2 elements
    if len(lst) > 2 and len(set(x for x in lst if lst.count(x) > 1)) > 0:
        return False
    # Check if the list has 1 unique element (handle edge case)
    if len(set(lst)) == 1:
        return True
    # Check if the list has 2 unique elements and the first element is smaller than the second
    if len(lst) == 2 and lst[0] < lst[1]:
        return True
    # Finally, the list has no duplicates and is already sorted
    return True