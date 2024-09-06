def is_sorted(lst):
    # Count the unique elements and sort the list if it contains multiple unique elements
    if len(set(lst)) > 1 and lst != sorted(lst):
        return False
    # Check if the list has at least two equal elements in it
    if len(lst) != len(set(lst)):
        return False
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            continue
        else:
            return False
    return True