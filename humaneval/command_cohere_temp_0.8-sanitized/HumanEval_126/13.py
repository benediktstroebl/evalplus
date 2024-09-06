def is_sorted(lst):
    # Count the unique elements and sort the list if it contains more than one unique element
    if len(set(lst)) > 1 and not lst == sorted(lst):
        return False
    # Check if the list contains duplicate elements by iterating and verifying the next element if the current element is repeated
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] and not i == 0:
            return False
    return True