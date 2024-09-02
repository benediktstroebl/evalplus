

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if not l1 or not l2:
        return []

    d = {}
    for num in l1:
        if num in d:
            d[num] += 1
            if d[num] > 1:
                d[num] -= 1
                if d[num] == 0:
                    d.pop(num)
        else:
            d[num] = 1

    result = []
    for num in l2:
        if num in d:
            result.append(num)
            d[num] -= 1
            if d[num] == 0:
                d.pop(num)
    return result
