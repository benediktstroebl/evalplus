
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    assert len(set(arr)) == len(arr), 'Invalid array'
    def find(element):
        for idx, el in enumerate(arr[:-1]):
            if element >= el:
                return idx
        return -1
    return find

