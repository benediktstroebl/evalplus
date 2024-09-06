

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    #l1 = l[:]
    l1 = l[:]
    if l1 == l1[::-1]:
        l1.pop(0)
        return max(l1)
    if l1 == l1[::-1]:
        l1.pop(-1)
        return max(l1)
    else:
        max_elem = l1[0]
        for i in l1:
            if i > max_elem:
                max_elem = i
        return max_elem
    
