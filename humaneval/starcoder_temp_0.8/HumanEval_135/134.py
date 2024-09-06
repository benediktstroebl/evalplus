
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def arrange(array):
        """
        Time complexity: 0(n)
        Space complexity: 0(1)
        """
        if len(array) == 0:
            return -1

        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                return i
        return -1

    return arrange(arr)

