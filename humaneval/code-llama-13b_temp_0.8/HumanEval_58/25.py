

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if not l1 or not l2:
        return []

    def to_hash(l):
        hash_t = {}
        for item in l:
            if item in hash_t:
                hash_t[item] += 1
            else:
                hash_t[item] = 1
        return hash_t

    hash_t1 = to_hash(l1)
    hash_t2 = to_hash(l2)

    result = []
    for item in hash_t1.keys():
        if item in hash_t2 and hash_t2[item] > 0:
            result.append(item)
            hash_t2[item] = 0
    return sorted(result)

