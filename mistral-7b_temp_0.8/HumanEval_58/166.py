

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    if not l1 or not l2:
        return []

    sorted_l1 = sorted(l1)
    sorted_l2 = sorted(l2)

    p1 = 0
    p2 = 0

    elements = []

    while p1 < len(sorted_l1) and p2 < len(sorted_l2):
        if sorted_l1[p1] < sorted_l2[p2]:
            p1 += 1
        elif sorted_l2[p2] < sorted_l1[p1]:
            p2 += 1
        else:
            elements.append(sorted_l1[p1])
            p1 += 1
            p2 += 1

    return elements

