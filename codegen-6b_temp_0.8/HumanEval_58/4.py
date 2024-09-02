

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # Method 1
    # return list(set(l1).intersection(set(l2)))

    # Method 2
    # sorted_l1 = sorted(l1)
    # sorted_l2 = sorted(l2)
    # smaller_list = min(len(sorted_l1), len(sorted_l2))
    # for i in range(0, smaller_list):
    #     if sorted_l1[i] == sorted_l2[i]:
    #         return [sorted_l1[i]] + common(sorted_l1[i:], sorted_l2[i:])
    # return sorted_l1[smaller_list:] + sorted_l2[smaller_list:]

    # Method 3
    dict1 = {}
    dict2 = {}
    for element in l1:
        dict1[element] = 1
    for element in l2:
        dict2[element] = 1
    return list(dict1.keys() & dict2.keys())

