

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # 1. if there is only one element in the list
    if len(l) == 1:
        return l[0]
    # 2. if there is more than one element in the list
    elif len(l) > 1:
        # 2.1 set max element to the first element
        max_element = l[0]
        # 2.2 if the second element is greater than the first element, then
        # set the second element to max element
        if max_element < l[1]:
            max_element = l[1]
        # 2.3 if the max element of the list is less than the rest of the
        # elements, then assign that element to max element
        for i in range(2, len(l)):
            if max_element < l[i]:
                max_element = l[i]
        return max_element

