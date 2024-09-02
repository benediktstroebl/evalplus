

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # first we build a dict for l1 with occurrences as values
    occurence_dict = dict()
    for item in l1:
        if item in occurence_dict.keys():
            occurence_dict[item] += 1
        else:
            occurence_dict[item] = 1

    # then we check for each item in l2 if it exists in occurence dict and if it does, decrement it
    for item in l2:
        if item in occurence_dict.keys():
            occurence_dict[item] -= 1

    # then we filter out the items that have zero occurrences
    for item in occurence_dict.copy():
        if occurence_dict[item] <= 0:
            del occurence_dict[item]

    # and return the sorted keys of the dict, since we have removed all duplicates
    return sorted(occurence_dict.keys())

