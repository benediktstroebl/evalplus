
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # arr = [1,2,4,3,5]
    # Preceding element 0
    # arr = [0,1,2,3,4]
    # Preceding element 1
    # arr = [1,0,2,3,4]
    # Preceding element 2
    # arr = [1,2,0,3,4]
    # Preceding element 3
    # arr = [1,2,3,0,4]
    # Preceding element 4
    # arr = [1,2,3,4,0]
    # Preceding element 5

    # arr = [0, 1, 2, 3, 4]
    # Preceding element 0
    # arr = [1, 0, 2, 3, 4]
    # Preceding element 1
    # arr = [2, 1, 0, 3, 4]
    # Preceding element 2
    # arr = [2, 3, 1, 0, 4]
    # Preceding element 3
    # arr = [2, 3, 4, 1, 0]
    # Preceding element 4
    # arr = [2, 3, 4, 0, 1]

    # arr = [0, 1, 2, 3, 4]
    # Preceding element 0
    # arr = [1, 0, 2, 3, 4]
    # Preceding element 1
    # arr = [2, 1, 0, 3, 4]
    # Preceding element 2
    # arr = [2, 3, 1, 0, 4]
    # Preceding element 3
    # arr = [2, 3, 4, 1, 0]
    # Preceding element 4
    # arr = [2, 3, 4, 0, 1]
    # Preceding element 5
    # arr = [2, 3, 4, 1, 0]
    
