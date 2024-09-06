
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    def find_peak(arr):
        """Find the largest element in the array. The array will not have
        duplicates."""

        for i in range(len(arr)):
            if i == 0 or arr[i-1] < arr[i]:
                return arr[i]

    def arr_arrange(arr):
        """Check if the array can be arranged.

        Parameters
        ----------
        arr : array
            The array to be checked.

        Returns
        -------
        int
            The index of the largest element that is not greater than or
            equal to the element immediately preceding it. If no such element
            exists then return -1.
        """

        peak = find_peak(arr)
        for i in range(len(arr)):
            if arr[i] > peak and arr[i] >= arr[i+1]:
                return i
        return -1

    return arr_arrange(arr)

