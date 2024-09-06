

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # sort the input list
    l = sorted(l)
    # get the unique elements
    unique_elements = set(l)
    # get the indices of the unique elements
    unique_indices = list(range(len(unique_elements)))
    # create a list of the unique elements and their indices
    unique_indices_and_values = [(unique_elements[i], i) for i in unique_indices]
    # return the sorted unique elements and their indices
    return l[unique_indices_and_values]