def next_smallest(lst):
    # Sort the list and get the length
    lst.sort()
    num_elements = len(lst)

    # Check if there are at least two elements
    if num_elements < 2:
        return None

    # Check if there is exactly one element
    if num_elements == 1:
        return None

    # Return the second element
    return lst[-2]