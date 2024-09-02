

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # sort both lists
    l1.sort()
    l2.sort()

    # create a dictionary to map each element to its count in the two lists
    counts = {}
    for i in range(len(l1)):
        counts[l1[i]] = counts.get(l1[i], 0) + 1
        counts[l2[i]] = counts.get(l2[i], 0) + 1

    # get the sorted unique elements and their count
    unique_counts = sorted(counts.items(), key=lambda x: x[1])

    # get the unique elements
    unique_elements = [k[0] for k in unique_counts]

    # return the unique elements
    return unique_elements
