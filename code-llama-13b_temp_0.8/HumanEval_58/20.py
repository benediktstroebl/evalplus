

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if l1 == [] or l2 == []:
        return []

    # Convert the lists to set
    set1 = set(l1)
    set2 = set(l2)

    # If they have no common elements return []
    if len(set1.intersection(set2)) == 0:
        return []

    # Combine the two lists into one list
    combined_list = l1 + l2

    # Remove the duplicates from the combined list
    unique_list = set(combined_list)

    # Sort the list in ascending order
    sorted_list = sorted(unique_list)

    # return the sorted list
    return sorted_list

