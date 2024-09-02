
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # print "About to sort"
    arr.sort()
    # print "Sorted"
    def find_nearest_num_with_ind(num):
        """Return the index of the smallest number greater than or equal to num."""
        # print "About to find outpredict idx"
        low = 0
        high = len(arr) - 1
        # print "Low and high:", low, high
        predicted_index = -1
        while low <= high:
            mid = low + (high-low)/2
            # print "mid:", mid
            if arr[mid] > num:
                high = mid - 1
            elif arr[mid] < num:
                low = mid + 1
            else:
                predicted_index = mid
        return predicted_index
    return find_nearest_num_with_ind
