
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    max_value = max(arr)
    if max_value > len(arr):
        return -1

    largest_index = max_value - 1
    largest_value = arr[largest_index]
    #print(largest_value)
    #print(largest_index)
    arr.sort(reverse=True)
    #print(arr)

    index = 0
    for i in range(len(arr)):
        if arr[i] <= largest_value:
            largest_index = i
            largest_value = arr[i]
            break
    return largest_index
