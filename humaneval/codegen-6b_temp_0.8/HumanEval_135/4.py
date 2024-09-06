
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Goes through each number in the array and finds the index of the max element
    # which is less than or equal to the previous element
    # For example [1,2,4,3,5]
    # 0 1 2 3 4
    # (-1,1,2,3,4)
    # (-1,1,2,4,3)
    # (-1,1,3,2,4)
    # (-1,1,3,4,2)
    # (-1,2,4,3,1)
    # (-1,2,4,1,3)
    # (-1,2,1,4,3)
    # (-1,2,1,3,4)
    # (-1,2,3,4,1)
    # (-1,2,3,1,4)
    # (-1,2,3,4,1)
    # (-1,3,2,4,1)
    # (-1,3,2,1,4)
    # (-1,3,2,4,1)
    # (-1,3,4,2,1)
    # (-1,3,4,1,2)
    # (-1,3,1,4,2)
    # (-1,3,1,2,4)
    # (-1,3,1,4,2)
    # (-1,3,4,1,2)
    # (-1,3,4,2,1)
    # 
    # if arr[i] < arr[i-1], it can't be the max element
    # Hence, we increment i, since arr[i] is greater than arr[i-1]
    #
    # we return the value of i - 1, since the previous max element is greater than
    # arr[i - 1]
    
    max_index = -1
    current_index = 0
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            # arr[i] = arr[i-1]
            current_index = i
        else:
            if max_index < current_index:
                