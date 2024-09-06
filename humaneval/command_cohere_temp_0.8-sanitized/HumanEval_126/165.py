def is_sorted(lst):
    # Count the unique elements and sort the list if it contains more than one unique element
    if len(set(lst)) > 1 and not lst == sorted(lst):
        return False
    # If exactly one unique element, it's sorted if it's a single element or a list of ascending integers of that element.
    if len(set(lst)) == 1: 
        return True
    # Check if it's a list of integers ascending from 1 with no duplicates
    return all(isinstance(n, int) for n in lst) and lst[0] == 1 and all(n == (n+1) for n in lst[1:])