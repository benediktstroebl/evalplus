

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # Sorting is a good practice. As we want to return the unique values, and
    # since we are dealing with integers, this way they will be sorted in
    # ascending order.
    l1_sorted = sorted(l1)
    l2_sorted = sorted(l2)

    # Comparing the lists one by one. This is done in the following way:
    # For every element in l1_sorted, we are searching for that element in
    # l2_sorted. If the element is present, we remove it from l2_sorted.
    # This way, we are building a smaller list, and then checking every
    # element in this list against every element in l1_sorted.
    # If an element is present in the built list, that means that
    # that element has been found in both lists. If this happens, we
    # append this element in a new list, that will store the common values.
    l_common = []
    for element in l1_sorted:
        if element in l2_sorted:
            l_common.append(element)
            l2_sorted.remove(element)
    return sorted(l_common)

