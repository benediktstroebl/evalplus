

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    seen1 = set()
    seen2 = set()
    for item1 in l1:
        if item1 not in seen1:
            seen1.add(item1)
            yield item1
    for item2 in l2:
        if item2 not in seen2:
            seen2.add(item2)
            yield item2
            break