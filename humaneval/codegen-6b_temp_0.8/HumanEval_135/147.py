
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    
    # Finds the last element which is less than or equal to the previous
    # element.
    def get_largest_index(arr):
        for i in range(1,len(arr)):
            if arr[i-1] < arr[i]:
                return i-1
        return -1
    
    # Gets the index of the first element
    def index_first(arr):
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > arr[i-1]:
                return i
    
    # Gets the index of the last element
    def index_last(arr):
        for i in range(1,len(arr)):
            if arr[i-1] < arr[i]:
                return i-1
    
    # Gets the index of the first element which is greater than the current
    def index_first_greater(arr, i):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                return j
    
    # Gets the index of the last element which is less than the current element
    def index_last_less(arr, i):
        for j in range(i, -1, -1):
            if arr[j] > arr[i]:
                return j
    
    # For each array element, check the index of the next element.
    # If the next element has an index > the current element's index, then
    # the sequence of elements is not possible. 
    # If the next element has an index <= the current element's index, then
    # the sequence of elements cannot be finished by the current element.
    # So find the index of the next element after the current element,
    # if any, and check for the index of the previous element.
    # If the previous element is < the next element, then the sequence cannot
    # be finished by the current element, as it needs to be finished by the
    # next element.
    def can_arrange_recursive(arr):
        for i in range(len(arr)-1):
            j = index_first_greater(arr, i)
            k = index_