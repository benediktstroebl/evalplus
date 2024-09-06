def is_sorted(lst):
    # Count the unique elements and sort the list if it contains more than one unique element
    if len(set(lst)) > 1 and not lst == sorted(lst):
        return False
    # Check if the elements are sorted if only one unique element exists in the list
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            continue
        else:
            return False
    return True