

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # assuming that the lists are sorted
    smaller = l1
    larger = l2
    if len(l1) < len(l2):
        smaller, larger = l2, l1
    # if not the lists are sorted
    if smaller[0] > larger[0]:
        smaller = sorted(smaller)
        larger = sorted(larger)

    # now both lists are sorted
    n1 = n2 = 0
    result = []
    while n1 < len(smaller) and n2 < len(larger):
        if smaller[n1] > larger[n2]:
            n2 += 1
        elif smaller[n1] < larger[n2]:
            n1 += 1
        else:
            result.append(smaller[n1])
            n1 += 1
            n2 += 1

    return result

