
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    
    if arr == sorted(arr): # if given array is already sorted
        return -1
    else:
        indices = [] # create empty list to store indices
        for i, val in enumerate(arr): # for each value in the array
            if arr[i] > arr[i - 1]: # if current value is greater than value before it
                indices.append(i) # append the index to the list
        if indices == []: # if indices list is empty
            return -1
        else:
            return max(indices) # return the highest index

