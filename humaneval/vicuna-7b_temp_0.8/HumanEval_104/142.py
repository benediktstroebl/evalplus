
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # convert input to list of integers
    x = set(map(int, x))

    # sort the set of integers in ascending order
    x.sort()

    # create a set of even integers
    evens = set(range(1, len(x)+1))

    # create a set of odd integers
    odds = set(range(2, len(x)+1))

    # find the intersection of the two sets
    inter = evens.intersection(odds)

    # find the union of the two sets
    union = evens.union(odds)

    # remove the elements from the set of integers that are in the inter
    # and union sets
    x.difference_update(inter)

    # add the elements from the union set that are not in the set of
    # integers to the list
    for el in union - x:
        x.add(el)

    return list(x)