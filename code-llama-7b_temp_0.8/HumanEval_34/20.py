

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # idea: Use the sorted method and check the previous element.

    # edge case: empty list
    if len(l) == 0:
        return []

    # base case: list with one item
    if len(l) == 1:
        return l

    # recursive case: we'll have 2 elements.
    if len(l) == 2:
        if l[0] == l[1]:
            return [l[0]]
        else:
            return l

    # we have a list with at least 3 items.
    # we'll divide the list into 3 parts.
    # 1st part: all elements that are smaller than the 2nd element.
    # 2nd part: the 2nd element (we'll return this part later)
    # 3rd part: all elements that are larger than the 2nd element.

    # Note: the 2nd element is the first element of the 2nd part
    #       and the last element of the 3rd part.

    # finding the 1st and 3rd part is easy, we'll just use slicing.
    first_part = l[:l.index(l[1])]
    third_part = l[l.index(l[1]) + 1:]

    # finding the 2nd part is a little bit harder
    # we'll try to find the largest element in the first part
    # that is smaller than the 2nd element

    # but we'll check the 1st element first.
    if l[0] < l[1]:
        second_part = [l[1]]
    else:
        second_part = [max(first_part)]

    # but if the 1st element is larger than the 2nd element, then the 2nd element
    # is the largest element in the first part.
    if l[0] > l[1]:
        second_part = [l[0]]

    # checking each element in the first part
    for i in range(1, len(first_part)):
        if first_part[i - 1] < l[1] <
