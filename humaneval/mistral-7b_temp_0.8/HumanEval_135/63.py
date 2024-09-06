
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # can't use list.sort() because of duplicate values

    # list.index() is O(n)

    # list.sort() is O(n log n)

    # Find smallest element using O(n)
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    # List comprehension
    # arr[arr.index(smallest) + 1:] is O(n)
    # sorted(arr[arr.index(smallest) + 1:]) is O(n log n)
    # len(sorted(arr[arr.index(smallest) + 1:]) is O(n)
    return arr[arr.index(smallest) + 1:].index(smallest) if arr.index(smallest) + 1 < len(arr) else -1
