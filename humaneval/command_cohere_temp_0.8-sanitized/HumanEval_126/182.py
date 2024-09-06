def is_sorted(lst):
    # Count the unique elements and sort the list if it contains multiple unique elements
    if len(set(lst)) > 1 and lst != sorted(lst):
        return False
    # Check if the list has duplicate elements by iterating and verifying if each element's next element is greater
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            return False
    return True