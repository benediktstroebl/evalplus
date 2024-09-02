

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # returns a list of unique values in a list
    # example: [5, 3, 5, 2, 3, 3, 9, 0, 123] => [0, 2, 3, 5, 9, 123]
    # time complexity is O(n)
    # space complexity is O(n)
    # does not use sets
    # uses dictionaries and the sorted() function
    # unique_set = set()
    # return [i for i in l if i not in unique_set and unique_set.add(i)]

    # solution 2
    # unique_set = set()
    # return sorted(list(set(l)))

    # solution 3
    # unique_set = set()
    # return [i for i in sorted(set(l))]

    # solution 4
    unique_set = set()
    return [i for i in sorted(l) if i not in unique_set and unique_set.add(i)]

