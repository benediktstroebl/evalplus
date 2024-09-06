
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    previous_elements = []

    for i, n in enumerate(arr):
        if len(previous_elements) == 0:
            previous_elements.append(n)
            continue

        if n < previous_elements[-1]:
            return i

        previous_elements.append(n)

    return -1

arrangement = can_arrange([1,2,3,4,5])

assert(arrangement == 3)

arrangement = can_arrange([1,1,1,1,1,1])

assert(arrangement == -1)

arrangement = can_arrange([0,0,0,0,0,0])

assert(arrangement == -1)
