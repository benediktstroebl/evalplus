
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    
    def create_function(arr):
        sorted_arr = sorted(arr)
        for index, element in enumerate(sorted_arr):
            if index!= len(sorted_arr) - 1:
                if element <= sorted_arr[index+1]:
                    return index
        return -1
    return create_function(arr)
