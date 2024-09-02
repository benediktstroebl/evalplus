
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Your code here
    # Your code here
    # return largest index of an element which is not greater than or equal to the element immediately preceding it
    # return -1 if no such element exists
    # array will not contain duplicate values
    if not arr:
        return -1

    # set visited to keep track of visited elements
    # set value to value of max index of the element not greater than it's preceding element
    # init value to -1
    visited = set()
    value = -1
    print(arr)
    print(len(arr))
    for index, num in enumerate(arr):
        print(index, num)
        # check if num not in visited
        # check if index not 0
        # and num < preceding element (arr[index-1])
        if num not in visited and index != 0 and num < arr[index - 1]:
            # set value to index
            value = index
            # add num to visited
            visited.add(num)

    return value



